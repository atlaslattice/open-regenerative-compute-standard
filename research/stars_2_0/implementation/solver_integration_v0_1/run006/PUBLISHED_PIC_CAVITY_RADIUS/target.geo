SetFactory("OpenCASCADE");
Geometry.Tolerance = 1e-10;
Sphere(1) = {0,0,0,520};
Sphere(2) = {0,0,0,500};
// Rotate CAD parameter seams only; spheres and physical geometry are unchanged.
Rotate { {0,1,0}, {0,0,0}, Pi/7 } { Volume{1,2}; }
shell[] = BooleanDifference{ Volume{1}; Delete; }{ Volume{2}; Delete; };
Cylinder(3) = {0,0,0,0,0,1040,100};
target[] = BooleanDifference{ Volume{shell[]}; Delete; }{ Volume{3}; Delete; };
Physical Volume("target_shell", 1) = {target[]};
boundary[] = Boundary{ Volume{target[]}; };
Physical Surface("unassigned_target_boundary", 2) = {boundary[]};
Mesh.CharacteristicLengthMin = 10;
Mesh.CharacteristicLengthMax = 10;
Mesh.Algorithm3D = 10;
Mesh.OptimizeNetgen = 1;
Mesh.MshFileVersion = 2.2;
Mesh.ScalingFactor = 1e-6;
