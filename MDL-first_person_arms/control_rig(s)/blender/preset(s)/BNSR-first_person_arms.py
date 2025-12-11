import bpy
import json
obj = bpy.context.object
scene = bpy.context.scene

# Bone Snapper Chains Data
scene.bone_snapper_chains_json = '''
[
  {
    "name": "Left Arm",
    "fk_bones": {
      "upper": "CRBN-first_person_arms-FK-arm_1.L",
      "middle": "CRBN-first_person_arms-FK-arm_2.L",
      "end": "CRBN-first_person_arms-FK-hand.L"
    },
    "mch_bones": {
      "upper": "CRBN-first_person_arms-MCH-arm_1.L",
      "middle": "CRBN-first_person_arms-MCH-arm_2.L",
      "end": "CRBN-first_person_arms-MCH-hand.L"
    },
    "ik_bones": {
      "pole": "CRBN-first_person_arms-POLE-arm_2.L",
      "target": "CRBN-first_person_arms-IK-hand.L"
    }
  },
  {
    "name": "Right Arm",
    "fk_bones": {
      "upper": "CRBN-first_person_arms-FK-arm_1.R",
      "middle": "CRBN-first_person_arms-FK-arm_2.R",
      "end": "CRBN-first_person_arms-FK-hand.R"
    },
    "mch_bones": {
      "upper": "CRBN-first_person_arms-MCH-arm_1.R",
      "middle": "CRBN-first_person_arms-MCH-arm_2.R",
      "end": "CRBN-first_person_arms-MCH-hand.R"
    },
    "ik_bones": {
      "pole": "CRBN-first_person_arms-POLE-arm_2.R",
      "target": "CRBN-first_person_arms-IK-hand.R"
    }
  },
  {
    "name": "Finger 1 Left",
    "fk_bones": {
      "upper": "CRBN-first_person_arms-CTRL-metacarpal_1.L",
      "middle": "CRBN-first_person_arms-FK-finger_1_phalanx_1.L",
      "end": "CRBN-first_person_arms-TWKR-finger_1_phalanx_2.L"
    },
    "mch_bones": {
      "upper": "CRBN-first_person_arms-MCH-metacarpal_1.L",
      "middle": "CRBN-first_person_arms-MCH-finger_1_phalanx_1.L",
      "end": "CRBN-first_person_arms-MCH-finger_1_phalanx_2.L"
    },
    "ik_bones": {
      "pole": "CRBN-first_person_arms-POLE-finger_1_phalanx_1.L",
      "target": "CRBN-first_person_arms-IK-finger_1_phalanx_2.L"
    }
  },
  {
    "name": "Finger 2 Left",
    "fk_bones": {
      "upper": "CRBN-first_person_arms-FK-finger_2_phalanx_1.L",
      "middle": "CRBN-first_person_arms-FK-finger_2_phalanx_2.L",
      "end": "CRBN-first_person_arms-TWKR-finger_2_phalanx_3.L"
    },
    "mch_bones": {
      "upper": "CRBN-first_person_arms-MCH-finger_2_phalanx_1.L",
      "middle": "CRBN-first_person_arms-MCH-finger_2_phalanx_2.L",
      "end": "CRBN-first_person_arms-MCH-finger_2_phalanx_3.L"
    },
    "ik_bones": {
      "pole": "CRBN-first_person_arms-POLE-finger_2_phalanx_2.L",
      "target": "CRBN-first_person_arms-IK-finger_2_phalanx_3.L"
    }
  },
  {
    "name": "Finger 3 Left",
    "fk_bones": {
      "upper": "CRBN-first_person_arms-FK-finger_3_phalanx_1.L",
      "middle": "CRBN-first_person_arms-FK-finger_3_phalanx_2.L",
      "end": "CRBN-first_person_arms-TWKR-finger_3_phalanx_3.L"
    },
    "mch_bones": {
      "upper": "CRBN-first_person_arms-MCH-finger_3_phalanx_1.L",
      "middle": "CRBN-first_person_arms-MCH-finger_3_phalanx_2.L",
      "end": "CRBN-first_person_arms-MCH-finger_3_phalanx_3.L"
    },
    "ik_bones": {
      "pole": "CRBN-first_person_arms-POLE-finger_3_phalanx_2.L",
      "target": "CRBN-first_person_arms-IK-finger_3_phalanx_3.L"
    }
  },
  {
    "name": "Finger 4 Left",
    "fk_bones": {
      "upper": "CRBN-first_person_arms-FK-finger_4_phalanx_1.L",
      "middle": "CRBN-first_person_arms-FK-finger_4_phalanx_2.L",
      "end": "CRBN-first_person_arms-TWKR-finger_4_phalanx_3.L"
    },
    "mch_bones": {
      "upper": "CRBN-first_person_arms-MCH-finger_4_phalanx_1.L",
      "middle": "CRBN-first_person_arms-MCH-finger_4_phalanx_2.L",
      "end": "CRBN-first_person_arms-MCH-finger_4_phalanx_3.L"
    },
    "ik_bones": {
      "pole": "CRBN-first_person_arms-POLE-finger_4_phalanx_2.L",
      "target": "CRBN-first_person_arms-IK-finger_4_phalanx_3.L"
    }
  },
  {
    "name": "Finger 5 Left",
    "fk_bones": {
      "upper": "CRBN-first_person_arms-FK-finger_5_phalanx_1.L",
      "middle": "CRBN-first_person_arms-FK-finger_5_phalanx_2.L",
      "end": "CRBN-first_person_arms-TWKR-finger_5_phalanx_3.L"
    },
    "mch_bones": {
      "upper": "CRBN-first_person_arms-MCH-finger_5_phalanx_1.L",
      "middle": "CRBN-first_person_arms-MCH-finger_5_phalanx_2.L",
      "end": "CRBN-first_person_arms-MCH-finger_5_phalanx_3.L"
    },
    "ik_bones": {
      "pole": "CRBN-first_person_arms-POLE-finger_5_phalanx_2.L",
      "target": "CRBN-first_person_arms-IK-finger_5_phalanx_3.L"
    }
  },
  {
    "name": "Finger 1 Right",
    "fk_bones": {
      "upper": "CRBN-first_person_arms-CTRL-metacarpal_1.R",
      "middle": "CRBN-first_person_arms-FK-finger_1_phalanx_1.R",
      "end": "CRBN-first_person_arms-TWKR-finger_1_phalanx_2.R"
    },
    "mch_bones": {
      "upper": "CRBN-first_person_arms-MCH-metacarpal_1.R",
      "middle": "CRBN-first_person_arms-MCH-finger_1_phalanx_1.R",
      "end": "CRBN-first_person_arms-MCH-finger_1_phalanx_2.R"
    },
    "ik_bones": {
      "pole": "CRBN-first_person_arms-POLE-finger_1_phalanx_1.R",
      "target": "CRBN-first_person_arms-IK-finger_1_phalanx_2.R"
    }
  },
  {
    "name": "Finger 2 Right",
    "fk_bones": {
      "upper": "CRBN-first_person_arms-FK-finger_2_phalanx_1.R",
      "middle": "CRBN-first_person_arms-FK-finger_2_phalanx_2.R",
      "end": "CRBN-first_person_arms-TWKR-finger_2_phalanx_3.R"
    },
    "mch_bones": {
      "upper": "CRBN-first_person_arms-MCH-finger_2_phalanx_1.R",
      "middle": "CRBN-first_person_arms-MCH-finger_2_phalanx_2.R",
      "end": "CRBN-first_person_arms-MCH-finger_2_phalanx_3.R"
    },
    "ik_bones": {
      "pole": "CRBN-first_person_arms-POLE-finger_2_phalanx_2.R",
      "target": "CRBN-first_person_arms-IK-finger_2_phalanx_3.R"
    }
  },
  {
    "name": "Finger 3 Right",
    "fk_bones": {
      "upper": "CRBN-first_person_arms-FK-finger_3_phalanx_1.R",
      "middle": "CRBN-first_person_arms-FK-finger_3_phalanx_2.R",
      "end": "CRBN-first_person_arms-TWKR-finger_3_phalanx_3.R"
    },
    "mch_bones": {
      "upper": "CRBN-first_person_arms-MCH-finger_3_phalanx_1.R",
      "middle": "CRBN-first_person_arms-MCH-finger_3_phalanx_2.R",
      "end": "CRBN-first_person_arms-MCH-finger_3_phalanx_3.R"
    },
    "ik_bones": {
      "pole": "CRBN-first_person_arms-POLE-finger_3_phalanx_2.R",
      "target": "CRBN-first_person_arms-IK-finger_3_phalanx_3.R"
    }
  },
  {
    "name": "Finger 4 Right",
    "fk_bones": {
      "upper": "CRBN-first_person_arms-FK-finger_4_phalanx_1.R",
      "middle": "CRBN-first_person_arms-FK-finger_4_phalanx_2.R",
      "end": "CRBN-first_person_arms-TWKR-finger_4_phalanx_3.R"
    },
    "mch_bones": {
      "upper": "CRBN-first_person_arms-MCH-finger_4_phalanx_1.R",
      "middle": "CRBN-first_person_arms-MCH-finger_4_phalanx_2.R",
      "end": "CRBN-first_person_arms-MCH-finger_4_phalanx_3.R"
    },
    "ik_bones": {
      "pole": "CRBN-first_person_arms-POLE-finger_4_phalanx_2.R",
      "target": "CRBN-first_person_arms-IK-finger_4_phalanx_3.R"
    }
  },
  {
    "name": "Finger 5 Right",
    "fk_bones": {
      "upper": "CRBN-first_person_arms-FK-finger_5_phalanx_1.R",
      "middle": "CRBN-first_person_arms-FK-finger_5_phalanx_2.R",
      "end": "CRBN-first_person_arms-TWKR-finger_5_phalanx_3.R"
    },
    "mch_bones": {
      "upper": "CRBN-first_person_arms-MCH-finger_5_phalanx_1.R",
      "middle": "CRBN-first_person_arms-MCH-finger_5_phalanx_2.R",
      "end": "CRBN-first_person_arms-MCH-finger_5_phalanx_3.R"
    },
    "ik_bones": {
      "pole": "CRBN-first_person_arms-POLE-finger_5_phalanx_2.R",
      "target": "CRBN-first_person_arms-IK-finger_5_phalanx_3.R"
    }
  }
]
'''