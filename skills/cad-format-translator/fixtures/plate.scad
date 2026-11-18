// Synthetic millimetre fixture. Origin is the lower left bottom corner.
bore = 10;
$fn = 96;
difference() {
    cube([60, 40, 10]);
    translate([17, 23, -1]) cylinder(h=12, d=bore);
}
