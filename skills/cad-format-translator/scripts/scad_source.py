"""Translate a bounded SCAD grammar into an editable CadQuery Python program."""

import keyword
import math
import re

TOKEN = re.compile(
    r"//[^\n]*|/\*.*?\*/|\s+|\$fn|[A-Za-z_]\w*|(?:\d+\.\d*|\.\d+|\d+)(?:[eE][+-]?\d+)?|[][(){}=,;+-]|.",
    re.S,
)


class Parser:
    def __init__(self, text, filename, analytic):
        self.tokens = []
        line = 1
        for m in TOKEN.finditer(text):
            token = m.group()
            if not token.isspace() and not token.startswith(("//", "/*")):
                self.tokens.append((token, line))
            line += token.count("\n")
        self.tokens.append(("", line))
        self.i = 0
        self.filename = filename
        self.parameters = {}
        self.numbers = {}
        self.facets = None
        self.analytic = analytic

    def peek(self):
        return self.tokens[self.i][0]

    def fail(self, message):
        raise ValueError(f"{self.filename}:{self.tokens[self.i][1]}: {message}")

    def take(self, token):
        if self.peek() != token:
            self.fail(f"expected {token!r}, found {self.peek()!r}")
        self.i += 1

    def scalar(self):
        sign = ""
        if self.peek() in ("+", "-"):
            sign = self.peek()
            self.take(sign)
        value = self.peek()
        if value in self.parameters:
            self.take(value)
            return sign + value
        try:
            number = float(value)
        except ValueError:
            self.fail(f"unsupported scalar or undefined parameter {value!r}")
        if not math.isfinite(number) or not value[0].isdigit() and value[0] != ".":
            self.fail("expected a finite literal")
        self.take(value)
        return sign + repr(number)

    def number(self, expression):
        token = expression.lstrip("+-")
        value = self.numbers[token] if token in self.numbers else float(token)
        return -value if expression.startswith("-") else value

    def positive(self, expression):
        if self.number(expression) <= 0:
            self.fail("this translation requires a positive dimension")
        return expression

    def vector(self, size=3, dimensions=False):
        self.take("[")
        values = [self.scalar()]
        for _ in range(size - 1):
            self.take(",")
            values.append(self.scalar())
        self.take("]")
        return (
            ", ".join(self.positive(v) for v in values)
            if dimensions
            else ", ".join(values)
        )

    def shape(self):
        op = self.peek()
        if op not in ("cube", "cylinder", "translate", "difference", "linear_extrude"):
            self.fail(f"unsupported SCAD operation {op!r}")
        self.take(op)
        self.take("(")
        if op == "difference":
            self.take(")")
            self.take("{")
            result = self.shape()
            while self.peek() != "}":
                result += ".cut(" + self.shape() + ")"
            self.take("}")
            return result
        if op == "linear_extrude":
            self.take("height")
            self.take("=")
            height = self.positive(self.scalar())
            self.take(")")
            self.take("square")
            self.take("(")
            dimensions = self.vector(2, dimensions=True)
            self.take(")")
            self.take(";")
            return f"cq.Workplane('XY').rect({dimensions}, centered=False).extrude({height})"
        if op == "cylinder":
            values = {}
            for idx in range(2):
                key = self.peek()
                if key not in ("h", "d") or key in values:
                    self.fail("expected named cylinder h and d")
                self.take(key)
                self.take("=")
                values[key] = self.positive(self.scalar())
                if idx == 0:
                    self.take(",")
            self.take(")")
            self.take(";")
            if self.analytic:
                return f"cq.Workplane('XY').circle(({values['d']}) / 2).extrude({values['h']})"
            if self.facets is None:
                self.fail("faceted cylinder requires explicit integer $fn >= 3")
            return f"cq.Workplane('XY').polygon({self.facets}, {values['d']}).extrude({values['h']})"
        vector = self.vector(dimensions=op == "cube")
        self.take(")")
        if op == "translate":
            return self.shape() + f".translate(({vector}))"
        self.take(";")
        return f"cq.Workplane('XY').box({vector}, centered=(False, False, False))"

    def program(self):
        while self.i + 1 < len(self.tokens) and self.tokens[self.i + 1][0] == "=":
            name = self.peek()
            if name != "$fn" and (
                not name.isidentifier()
                or keyword.iskeyword(name)
                or name in ("cq", "model", "build_model")
                or name in self.parameters
            ):
                self.fail(f"unsupported or repeated parameter {name!r}")
            self.take(name)
            self.take("=")
            if name == "$fn":
                token = self.peek()
                if self.facets is not None or not token.isdecimal() or int(token) < 3:
                    self.fail("expected a single fixed $fn >= 3")
                self.facets = int(token)
                self.take(token)
            else:
                value = self.scalar()
                self.numbers[name] = self.number(value)
                self.parameters[name] = value
            self.take(";")
        shape = self.shape()
        if self.peek():
            self.fail("unsupported trailing statement")
        lines = [
            '"""Editable generator translated from the supported SCAD subset; units mm."""',
            "import cadquery as cq",
            "",
        ]
        lines.extend(f"{key} = {value}" for key, value in self.parameters.items())
        lines.extend(
            [
                "",
                "def build_model():",
                "    return " + shape,
                "",
                "model = build_model()",
                "",
            ]
        )
        return "\n".join(lines)


def translate(text, filename, analytic=False):
    return Parser(text, filename, analytic).program()
