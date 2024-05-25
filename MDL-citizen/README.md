# Citizen Control Rig v0.3

Use only with the latest version of Blender.

Please read this [page](https://wiki.facepunch.com/sbox/Citizen_Model) and this [page](https://wiki.facepunch.com/sbox/First_Person) in order to understand better how the citizen.vmdl works.

This control rig drives the already existing skeleton from the citizen.vmdl file provided by [Facepunch](https://facepunch.com), meaning that it doesn't use a different skeleton and however the animation may be displayed in Blender, it will be displayed with the same accuracy in ModelDoc (that is once the twist and helper bones are configured in Blender).

# Features

* Exported animations are directly compatible with the provided citizen.vmdl by Facepunch.
* Advanced Head, Spine & Foot Controls Systems.
* Standard IK & Pole System.
* Standard Camera System (On the Control Rig only) in case you want to animate viewmodel animations on the Citizen Control Rig then transfer it to the First Person Citizen Control Rig and tweak it.
* Added Twist Control System from ModelDoc (This is only in case the twist control bones will be added to citizen.fbx. Even if you animate these, they won't do anything.).
* Custom Bone Shapes.
* Custom Bone Groups and Colors.
* Custom Naming Conventions.
* Very organized collection hierarchy meant to be easily appended into other .blend files without colliding with the naming conventions of other already existing collections.
* Near perfect accuracy to the in-game skeleton (In terms of bone transforms).
* Adapted all the skeleton poses to the control rig.
* Materials use textures provided by Facepunch.
* Perfect re-creation of the TiltTwist System and other systems from ModelDoc to Blender.
* All animations to be adapted to the control rig.
* IK to FK & FK to IK Snap System.

# To be added

* Advanced Facial Morph System based on drivers.