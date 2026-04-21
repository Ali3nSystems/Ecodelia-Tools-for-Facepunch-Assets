import bpy
import json
obj = bpy.context.object
scene = bpy.context.scene

# Bone Snapper Chains Data
scene.bone_snapper_chains_json = '''
[
  {
    "name": "Finger 1 Left",
    "fk_bones": {
      "upper": "CRBN-human-CTRL-metacarpal_1.L",
      "middle": "CRBN-human-FK-finger_1_phalanx_1.L",
      "end": "CRBN-human-TWKR-finger_1_phalanx_2.L"
    },
    "mch_bones": {
      "upper": "CRBN-human-MCH-metacarpal_1.L",
      "middle": "CRBN-human-MCH-finger_1_phalanx_1.L",
      "end": "CRBN-human-MCH-finger_1_phalanx_2.L"
    },
    "ik_bones": {
      "pole": "CRBN-human-POLE-finger_1_phalanx_1.L",
      "target": "CRBN-human-IK-finger_1_phalanx_2.L"
    }
  },
  {
    "name": "Finger 2 Left",
    "fk_bones": {
      "upper": "CRBN-human-FK-finger_2_phalanx_1.L",
      "middle": "CRBN-human-FK-finger_2_phalanx_2.L",
      "end": "CRBN-human-TWKR-finger_2_phalanx_3.L"
    },
    "mch_bones": {
      "upper": "CRBN-human-MCH-finger_2_phalanx_1.L",
      "middle": "CRBN-human-MCH-finger_2_phalanx_2.L",
      "end": "CRBN-human-MCH-finger_2_phalanx_3.L"
    },
    "ik_bones": {
      "pole": "CRBN-human-POLE-finger_2_phalanx_2.L",
      "target": "CRBN-human-IK-finger_2_phalanx_3.L"
    }
  },
  {
    "name": "Finger 3 Left",
    "fk_bones": {
      "upper": "CRBN-human-FK-finger_3_phalanx_1.L",
      "middle": "CRBN-human-FK-finger_3_phalanx_2.L",
      "end": "CRBN-human-TWKR-finger_3_phalanx_3.L"
    },
    "mch_bones": {
      "upper": "CRBN-human-MCH-finger_3_phalanx_1.L",
      "middle": "CRBN-human-MCH-finger_3_phalanx_2.L",
      "end": "CRBN-human-MCH-finger_3_phalanx_3.L"
    },
    "ik_bones": {
      "pole": "CRBN-human-POLE-finger_3_phalanx_2.L",
      "target": "CRBN-human-IK-finger_3_phalanx_3.L"
    }
  },
  {
    "name": "Finger 4 Left",
    "fk_bones": {
      "upper": "CRBN-human-FK-finger_4_phalanx_1.L",
      "middle": "CRBN-human-FK-finger_4_phalanx_2.L",
      "end": "CRBN-human-TWKR-finger_4_phalanx_3.L"
    },
    "mch_bones": {
      "upper": "CRBN-human-MCH-finger_4_phalanx_1.L",
      "middle": "CRBN-human-MCH-finger_4_phalanx_2.L",
      "end": "CRBN-human-MCH-finger_4_phalanx_3.L"
    },
    "ik_bones": {
      "pole": "CRBN-human-POLE-finger_4_phalanx_2.L",
      "target": "CRBN-human-IK-finger_4_phalanx_3.L"
    }
  },
  {
    "name": "Finger 5 Left",
    "fk_bones": {
      "upper": "CRBN-human-FK-finger_5_phalanx_1.L",
      "middle": "CRBN-human-FK-finger_5_phalanx_2.L",
      "end": "CRBN-human-TWKR-finger_5_phalanx_3.L"
    },
    "mch_bones": {
      "upper": "CRBN-human-MCH-finger_5_phalanx_1.L",
      "middle": "CRBN-human-MCH-finger_5_phalanx_2.L",
      "end": "CRBN-human-MCH-finger_5_phalanx_3.L"
    },
    "ik_bones": {
      "pole": "CRBN-human-POLE-finger_5_phalanx_2.L",
      "target": "CRBN-human-IK-finger_5_phalanx_3.L"
    }
  },
  {
    "name": "Finger 1 Right",
    "fk_bones": {
      "upper": "CRBN-human-CTRL-metacarpal_1.R",
      "middle": "CRBN-human-FK-finger_1_phalanx_1.R",
      "end": "CRBN-human-TWKR-finger_1_phalanx_2.R"
    },
    "mch_bones": {
      "upper": "CRBN-human-MCH-metacarpal_1.R",
      "middle": "CRBN-human-MCH-finger_1_phalanx_1.R",
      "end": "CRBN-human-MCH-finger_1_phalanx_2.R"
    },
    "ik_bones": {
      "pole": "CRBN-human-POLE-finger_1_phalanx_1.R",
      "target": "CRBN-human-IK-finger_1_phalanx_2.R"
    }
  },
  {
    "name": "Finger 2 Right",
    "fk_bones": {
      "upper": "CRBN-human-FK-finger_2_phalanx_1.R",
      "middle": "CRBN-human-FK-finger_2_phalanx_2.R",
      "end": "CRBN-human-TWKR-finger_2_phalanx_3.R"
    },
    "mch_bones": {
      "upper": "CRBN-human-MCH-finger_2_phalanx_1.R",
      "middle": "CRBN-human-MCH-finger_2_phalanx_2.R",
      "end": "CRBN-human-MCH-finger_2_phalanx_3.R"
    },
    "ik_bones": {
      "pole": "CRBN-human-POLE-finger_2_phalanx_2.R",
      "target": "CRBN-human-IK-finger_2_phalanx_3.R"
    }
  },
  {
    "name": "Finger 3 Right",
    "fk_bones": {
      "upper": "CRBN-human-FK-finger_3_phalanx_1.R",
      "middle": "CRBN-human-FK-finger_3_phalanx_2.R",
      "end": "CRBN-human-TWKR-finger_3_phalanx_3.R"
    },
    "mch_bones": {
      "upper": "CRBN-human-MCH-finger_3_phalanx_1.R",
      "middle": "CRBN-human-MCH-finger_3_phalanx_2.R",
      "end": "CRBN-human-MCH-finger_3_phalanx_3.R"
    },
    "ik_bones": {
      "pole": "CRBN-human-POLE-finger_3_phalanx_2.R",
      "target": "CRBN-human-IK-finger_3_phalanx_3.R"
    }
  },
  {
    "name": "Finger 4 Right",
    "fk_bones": {
      "upper": "CRBN-human-FK-finger_4_phalanx_1.R",
      "middle": "CRBN-human-FK-finger_4_phalanx_2.R",
      "end": "CRBN-human-TWKR-finger_4_phalanx_3.R"
    },
    "mch_bones": {
      "upper": "CRBN-human-MCH-finger_4_phalanx_1.R",
      "middle": "CRBN-human-MCH-finger_4_phalanx_2.R",
      "end": "CRBN-human-MCH-finger_4_phalanx_3.R"
    },
    "ik_bones": {
      "pole": "CRBN-human-POLE-finger_4_phalanx_2.R",
      "target": "CRBN-human-IK-finger_4_phalanx_3.R"
    }
  },
  {
    "name": "Finger 5 Right",
    "fk_bones": {
      "upper": "CRBN-human-FK-finger_5_phalanx_1.R",
      "middle": "CRBN-human-FK-finger_5_phalanx_2.R",
      "end": "CRBN-human-TWKR-finger_5_phalanx_3.R"
    },
    "mch_bones": {
      "upper": "CRBN-human-MCH-finger_5_phalanx_1.R",
      "middle": "CRBN-human-MCH-finger_5_phalanx_2.R",
      "end": "CRBN-human-MCH-finger_5_phalanx_3.R"
    },
    "ik_bones": {
      "pole": "CRBN-human-POLE-finger_5_phalanx_2.R",
      "target": "CRBN-human-IK-finger_5_phalanx_3.R"
    }
  },
  {
    "name": "Left Arm",
    "fk_bones": {
      "upper": "CRBN-human-FK-arm_1.L",
      "middle": "CRBN-human-FK-arm_2.L",
      "end": "CRBN-human-FK-hand.L"
    },
    "mch_bones": {
      "upper": "CRBN-human-MCH-arm_1.L",
      "middle": "CRBN-human-MCH-arm_2.L",
      "end": "CRBN-human-MCH-hand.L"
    },
    "ik_bones": {
      "pole": "CRBN-human-POLE-arm_2.L",
      "target": "CRBN-human-IK-hand.L"
    }
  },
  {
    "name": "Right Arm",
    "fk_bones": {
      "upper": "CRBN-human-FK-arm_1.R",
      "middle": "CRBN-human-FK-arm_2.R",
      "end": "CRBN-human-FK-hand.R"
    },
    "mch_bones": {
      "upper": "CRBN-human-MCH-arm_1.R",
      "middle": "CRBN-human-MCH-arm_2.R",
      "end": "CRBN-human-MCH-hand.R"
    },
    "ik_bones": {
      "pole": "CRBN-human-POLE-arm_2.R",
      "target": "CRBN-human-IK-hand.R"
    }
  },
  {
    "name": "Left Leg",
    "fk_bones": {
      "upper": "CRBN-human-FK-leg_1.L",
      "middle": "CRBN-human-FK-leg_2.L",
      "end": "CRBN-human-FK-foot.L"
    },
    "mch_bones": {
      "upper": "CRBN-human-MCH-leg_1.L",
      "middle": "CRBN-human-MCH-leg_2.L",
      "end": "CRBN-human-MCH-foot.L"
    },
    "ik_bones": {
      "pole": "CRBN-human-POLE-leg_2.L",
      "target": "CRBN-human-IK-foot.L"
    }
  },
  {
    "name": "Right leg",
    "fk_bones": {
      "upper": "CRBN-human-FK-leg_1.R",
      "middle": "CRBN-human-FK-leg_2.R",
      "end": "CRBN-human-FK-foot.R"
    },
    "mch_bones": {
      "upper": "CRBN-human-MCH-leg_1.R",
      "middle": "CRBN-human-MCH-leg_2.R",
      "end": "CRBN-human-MCH-foot.R"
    },
    "ik_bones": {
      "pole": "CRBN-human-POLE-leg_2.R",
      "target": "CRBN-human-IK-foot.R"
    }
  }
]
'''