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
      "upper": "CRBN-citizen-CTRL-metacarpal_1.L",
      "middle": "CRBN-citizen-FK-finger_1_phalanx_1.L",
      "end": "CRBN-citizen-TWKR-finger_1_phalanx_2.L"
    },
    "mch_bones": {
      "upper": "CRBN-citizen-MCH-metacarpal_1.L",
      "middle": "CRBN-citizen-MCH-finger_1_phalanx_1.L",
      "end": "CRBN-citizen-MCH-finger_1_phalanx_2.L"
    },
    "ik_bones": {
      "pole": "CRBN-citizen-POLE-finger_1_phalanx_1.L",
      "target": "CRBN-citizen-IK-finger_1_phalanx_2.L"
    }
  },
  {
    "name": "Finger 2 Left",
    "fk_bones": {
      "upper": "CRBN-citizen-FK-finger_2_phalanx_1.L",
      "middle": "CRBN-citizen-FK-finger_2_phalanx_2.L",
      "end": "CRBN-citizen-TWKR-finger_2_phalanx_3.L"
    },
    "mch_bones": {
      "upper": "CRBN-citizen-MCH-finger_2_phalanx_1.L",
      "middle": "CRBN-citizen-MCH-finger_2_phalanx_2.L",
      "end": "CRBN-citizen-MCH-finger_2_phalanx_3.L"
    },
    "ik_bones": {
      "pole": "CRBN-citizen-POLE-finger_2_phalanx_2.L",
      "target": "CRBN-citizen-IK-finger_2_phalanx_3.L"
    }
  },
  {
    "name": "Finger 3 Left",
    "fk_bones": {
      "upper": "CRBN-citizen-FK-finger_3_phalanx_1.L",
      "middle": "CRBN-citizen-FK-finger_3_phalanx_2.L",
      "end": "CRBN-citizen-TWKR-finger_3_phalanx_3.L"
    },
    "mch_bones": {
      "upper": "CRBN-citizen-MCH-finger_3_phalanx_1.L",
      "middle": "CRBN-citizen-MCH-finger_3_phalanx_2.L",
      "end": "CRBN-citizen-MCH-finger_3_phalanx_3.L"
    },
    "ik_bones": {
      "pole": "CRBN-citizen-POLE-finger_3_phalanx_2.L",
      "target": "CRBN-citizen-IK-finger_3_phalanx_3.L"
    }
  },
  {
    "name": "Finger 4 Left",
    "fk_bones": {
      "upper": "CRBN-citizen-FK-finger_4_phalanx_1.L",
      "middle": "CRBN-citizen-FK-finger_4_phalanx_2.L",
      "end": "CRBN-citizen-TWKR-finger_4_phalanx_3.L"
    },
    "mch_bones": {
      "upper": "CRBN-citizen-MCH-finger_4_phalanx_1.L",
      "middle": "CRBN-citizen-MCH-finger_4_phalanx_2.L",
      "end": "CRBN-citizen-MCH-finger_4_phalanx_3.L"
    },
    "ik_bones": {
      "pole": "CRBN-citizen-POLE-finger_4_phalanx_2.L",
      "target": "CRBN-citizen-IK-finger_4_phalanx_3.L"
    }
  },
  {
    "name": "Finger 1 Right",
    "fk_bones": {
      "upper": "CRBN-citizen-CTRL-metacarpal_1.R",
      "middle": "CRBN-citizen-FK-finger_1_phalanx_1.R",
      "end": "CRBN-citizen-TWKR-finger_1_phalanx_2.R"
    },
    "mch_bones": {
      "upper": "CRBN-citizen-MCH-metacarpal_1.R",
      "middle": "CRBN-citizen-MCH-finger_1_phalanx_1.R",
      "end": "CRBN-citizen-MCH-finger_1_phalanx_2.R"
    },
    "ik_bones": {
      "pole": "CRBN-citizen-POLE-finger_1_phalanx_1.R",
      "target": "CRBN-citizen-IK-finger_1_phalanx_2.R"
    }
  },
  {
    "name": "Finger 2 Right",
    "fk_bones": {
      "upper": "CRBN-citizen-FK-finger_2_phalanx_1.R",
      "middle": "CRBN-citizen-FK-finger_2_phalanx_2.R",
      "end": "CRBN-citizen-TWKR-finger_2_phalanx_3.R"
    },
    "mch_bones": {
      "upper": "CRBN-citizen-MCH-finger_2_phalanx_1.R",
      "middle": "CRBN-citizen-MCH-finger_2_phalanx_2.R",
      "end": "CRBN-citizen-MCH-finger_2_phalanx_3.R"
    },
    "ik_bones": {
      "pole": "CRBN-citizen-POLE-finger_2_phalanx_2.R",
      "target": "CRBN-citizen-IK-finger_2_phalanx_3.R"
    }
  },
  {
    "name": "Finger 3 Right",
    "fk_bones": {
      "upper": "CRBN-citizen-FK-finger_3_phalanx_1.R",
      "middle": "CRBN-citizen-FK-finger_3_phalanx_2.R",
      "end": "CRBN-citizen-TWKR-finger_3_phalanx_3.R"
    },
    "mch_bones": {
      "upper": "CRBN-citizen-MCH-finger_3_phalanx_1.R",
      "middle": "CRBN-citizen-MCH-finger_3_phalanx_2.R",
      "end": "CRBN-citizen-MCH-finger_3_phalanx_3.R"
    },
    "ik_bones": {
      "pole": "CRBN-citizen-POLE-finger_3_phalanx_2.R",
      "target": "CRBN-citizen-IK-finger_3_phalanx_3.R"
    }
  },
  {
    "name": "Finger 4 Right",
    "fk_bones": {
      "upper": "CRBN-citizen-FK-finger_4_phalanx_1.R",
      "middle": "CRBN-citizen-FK-finger_4_phalanx_2.R",
      "end": "CRBN-citizen-TWKR-finger_4_phalanx_3.R"
    },
    "mch_bones": {
      "upper": "CRBN-citizen-MCH-finger_4_phalanx_1.R",
      "middle": "CRBN-citizen-MCH-finger_4_phalanx_2.R",
      "end": "CRBN-citizen-MCH-finger_4_phalanx_3.R"
    },
    "ik_bones": {
      "pole": "CRBN-citizen-POLE-finger_4_phalanx_2.R",
      "target": "CRBN-citizen-IK-finger_4_phalanx_3.R"
    }
  },
  {
    "name": "Left Arm",
    "fk_bones": {
      "upper": "CRBN-citizen-FK-arm_1.L",
      "middle": "CRBN-citizen-FK-arm_2.L",
      "end": "CRBN-citizen-FK-hand.L"
    },
    "mch_bones": {
      "upper": "CRBN-citizen-MCH-arm_1.L",
      "middle": "CRBN-citizen-MCH-arm_2.L",
      "end": "CRBN-citizen-MCH-hand.L"
    },
    "ik_bones": {
      "pole": "CRBN-citizen-POLE-arm_2.L",
      "target": "CRBN-citizen-IK-hand.L"
    }
  },
  {
    "name": "Right Arm",
    "fk_bones": {
      "upper": "CRBN-citizen-FK-arm_1.R",
      "middle": "CRBN-citizen-FK-arm_2.R",
      "end": "CRBN-citizen-FK-hand.R"
    },
    "mch_bones": {
      "upper": "CRBN-citizen-MCH-arm_1.R",
      "middle": "CRBN-citizen-MCH-arm_2.R",
      "end": "CRBN-citizen-MCH-hand.R"
    },
    "ik_bones": {
      "pole": "CRBN-citizen-POLE-arm_2.R",
      "target": "CRBN-citizen-IK-hand.R"
    }
  },
  {
    "name": "Left Leg",
    "fk_bones": {
      "upper": "CRBN-citizen-FK-leg_1.L",
      "middle": "CRBN-citizen-FK-leg_2.L",
      "end": "CRBN-citizen-FK-foot.L"
    },
    "mch_bones": {
      "upper": "CRBN-citizen-MCH-leg_1.L",
      "middle": "CRBN-citizen-MCH-leg_2.L",
      "end": "CRBN-citizen-MCH-foot.L"
    },
    "ik_bones": {
      "pole": "CRBN-citizen-POLE-leg_2.L",
      "target": "CRBN-citizen-IK-foot.L"
    }
  },
  {
    "name": "Right leg",
    "fk_bones": {
      "upper": "CRBN-citizen-FK-leg_1.R",
      "middle": "CRBN-citizen-FK-leg_2.R",
      "end": "CRBN-citizen-FK-foot.R"
    },
    "mch_bones": {
      "upper": "CRBN-citizen-MCH-leg_1.R",
      "middle": "CRBN-citizen-MCH-leg_2.R",
      "end": "CRBN-citizen-MCH-foot.R"
    },
    "ik_bones": {
      "pole": "CRBN-citizen-POLE-leg_2.R",
      "target": "CRBN-citizen-IK-foot.R"
    }
  }
]
'''