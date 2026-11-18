"""Print entity and layer display settings for a DXF layout and nested blocks."""
import argparse
import json


def inventory(path, layout="Model", limit=100000):
    import ezdxf
    from ezdxf.addons.drawing.properties import RenderContext
    doc = ezdxf.readfile(path)
    space = doc.layouts.get(layout)
    ctx = RenderContext(doc)
    ctx.set_current_layout(space)
    rows = []
    cells = 0
    def visit(entities, trail, names, visible):
        nonlocal cells
        for entity in entities:
            if len(rows) >= limit:
                raise ValueError("occurrence limit exceeded")
            props = ctx.resolve_all(entity)
            key = trail + [entity.dxf.handle]
            show = visible and props.is_visible
            rows.append(dict(path=key, type=entity.dxftype(), layer=entity.dxf.layer,
                             effective_layer=props.layer, aci=entity.dxf.color,
                             true_colour=entity.dxf.get("true_color"), display_colour=props.color,
                             visible=show))
            if entity.dxftype() != "INSERT":
                continue
            name = entity.dxf.name.casefold()
            if name in names or len(names) >= 32 or entity.block() is None:
                raise ValueError(f"unresolved, cyclic or too deeply nested block at {key}")
            cells += entity.mcount
            if cells > limit:
                raise ValueError("block cell traversal limit exceeded")
            ctx.push_state(props)
            try:
                for cell in range(entity.mcount):
                    branch = key + [f"cell-{cell}"] if entity.mcount > 1 else key
                    visit(entity.block(), branch, names | {name}, show)
                visit(entity.attribs, key + ["attributes"], names, show)
            finally:
                ctx.pop_state()
    visit(space, [layout], set(), True)
    return dict(layout=layout, entities=rows, layers=[
        dict(name=x.dxf.name, aci=x.color, true_colour=x.dxf.get("true_color"),
             off=x.is_off(), frozen=x.is_frozen(), locked=x.is_locked()) for x in doc.layers])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source")
    parser.add_argument("--layout", default="Model")
    args = parser.parse_args()
    print(json.dumps(inventory(args.source, args.layout), indent=2))
