#October Dare 10/7/2018 - 48 Hour Challenge
import pygame, os, sys
pygame.init()
os.environ['SDL_VIDEO_WINDOW_POS'] = str(50) + "," + str(50)

screen = pygame.display.set_mode((1280,720)) #640,448
#screen = pygame.display.set_mode((640,448)) #640,448
clock = pygame.time.Clock()

##
oneTime = True
darknessCounter = 0
##
slashSound = pygame.mixer.Sound('slash001.wav')

#Load Images#
backgroundImage = pygame.image.load('blackBackground.png')
heartImage = pygame.image.load('hudImages/heart.png')
darkness000 = pygame.image.load('darkness000.png')
darkness001 = pygame.image.load('darkness001.png')
darkness002 = pygame.image.load('darkness002.png')

tile_1 = pygame.image.load('tileImages/Tile (1).png')
tile_2 = pygame.image.load('tileImages/Tile (2).png')
tile_3 = pygame.image.load('tileImages/Tile (3).png')
tile_4 = pygame.image.load('tileImages/Tile (4).png')
tile_5 = pygame.image.load('tileImages/Tile (5).png')
tile_6 = pygame.image.load('tileImages/Tile (6).png')
tile_7 = pygame.image.load('tileImages/Tile (7).png')
tile_8 = pygame.image.load('tileImages/Tile (8).png')
tile_9 = pygame.image.load('tileImages/Tile (9).png')

tile_10 = pygame.image.load('tileImages/Tile (10).png')
tile_11 = pygame.image.load('tileImages/Tile (11).png')
tile_12 = pygame.image.load('tileImages/Tile (12).png')
tile_13 = pygame.image.load('tileImages/Tile (13).png')
tile_14 = pygame.image.load('tileImages/Tile (14).png')
tile_15 = pygame.image.load('tileImages/Tile (15).png')
tile_16 = pygame.image.load('tileImages/Tile (16).png')
tile_17 = pygame.image.load('tileImages/Tile (17).png')
tile_18 = pygame.image.load('tileImages/Tile (18).png')
tile_19 = pygame.image.load('tileImages/Tile (19).png')

tile_20 = pygame.image.load('tileImages/Tile (20).png')
tile_21 = pygame.image.load('tileImages/Tile (21).png')
tile_22 = pygame.image.load('tileImages/Tile (22).png')
tile_23 = pygame.image.load('tileImages/Tile (23).png')
tile_24 = pygame.image.load('tileImages/Tile (24).png')
tile_25 = pygame.image.load('tileImages/Tile (25).png')
tile_26 = pygame.image.load('tileImages/Tile (26).png')
tile_27 = pygame.image.load('tileImages/Tile (27).png')
tile_28 = pygame.image.load('tileImages/Tile (28).png')
tile_29 = pygame.image.load('tileImages/Tile (29).png')

tile_30 = pygame.image.load('tileImages/Tile (30).png')
tile_31 = pygame.image.load('tileImages/Tile (31).png')
tile_32 = pygame.image.load('tileImages/Tile (32).png')
tile_33 = pygame.image.load('tileImages/Tile (33).png')
tile_34 = pygame.image.load('tileImages/Tile (34).png')
tile_35 = pygame.image.load('tileImages/Tile (35).png')
tile_36 = pygame.image.load('tileImages/Tile (36).png')
tile_37 = pygame.image.load('tileImages/Tile (37).png')
tile_38 = pygame.image.load('tileImages/Tile (38).png')
tile_39 = pygame.image.load('tileImages/Tile (39).png')

tile_40 = pygame.image.load('tileImages/Tile (40).png')
tile_41 = pygame.image.load('tileImages/Tile (41).png')
tile_42 = pygame.image.load('tileImages/Tile (42).png')
tile_43 = pygame.image.load('tileImages/Tile (43).png')
tile_44 = pygame.image.load('tileImages/Tile (44).png')
tile_45 = pygame.image.load('tileImages/Tile (45).png')
tile_46 = pygame.image.load('tileImages/Tile (46).png')
tile_47 = pygame.image.load('tileImages/Tile (47).png')
tile_48 = pygame.image.load('tileImages/Tile (48).png')
tile_49 = pygame.image.load('tileImages/Tile (49).png')

tile_50 = pygame.image.load('tileImages/Tile (50).png')
tile_51 = pygame.image.load('tileImages/Tile (51).png')
tile_52 = pygame.image.load('tileImages/Tile (52).png')
tile_53 = pygame.image.load('tileImages/Tile (53).png')
tile_54 = pygame.image.load('tileImages/Tile (54).png')
tile_55 = pygame.image.load('tileImages/Tile (55).png')
tile_56 = pygame.image.load('tileImages/Tile (56).png')
tile_57 = pygame.image.load('tileImages/Tile (57).png')
tile_58 = pygame.image.load('tileImages/Tile (58).png')
tile_59 = pygame.image.load('tileImages/Tile (59).png')

tile_60 = pygame.image.load('tileImages/Tile (60).png')
tile_61 = pygame.image.load('tileImages/Tile (61).png')
tile_62 = pygame.image.load('tileImages/Tile (62).png')
tile_63 = pygame.image.load('tileImages/Tile (63).png')
tile_64 = pygame.image.load('tileImages/Tile (64).png')
tile_65 = pygame.image.load('tileImages/Tile (65).png')
tile_66 = pygame.image.load('tileImages/Tile (66).png')
tile_67 = pygame.image.load('tileImages/Tile (67).png')
tile_68 = pygame.image.load('tileImages/Tile (68).png')
tile_69 = pygame.image.load('tileImages/Tile (69).png')

tile_70 = pygame.image.load('tileImages/Tile (70).png')
tile_71 = pygame.image.load('tileImages/Tile (71).png')
tile_72 = pygame.image.load('tileImages/Tile (72).png')
tile_73 = pygame.image.load('tileImages/Tile (73).png')
tile_74 = pygame.image.load('tileImages/Tile (74).png')
tile_75 = pygame.image.load('tileImages/Tile (75).png')
tile_76 = pygame.image.load('tileImages/Tile (76).png')
tile_77 = pygame.image.load('tileImages/Tile (77).png')
tile_78 = pygame.image.load('tileImages/Tile (78).png')
tile_79 = pygame.image.load('tileImages/Tile (79).png')

tile_80 = pygame.image.load('tileImages/Tile (80).png')
tile_81 = pygame.image.load('tileImages/Tile (81).png')
tile_82 = pygame.image.load('tileImages/Tile (82).png')
tile_83 = pygame.image.load('tileImages/Tile (83).png')

#PLAYER
frontIdle_000 = pygame.image.load('playerImages/Front - Idle_000.png')
frontIdle_001 = pygame.image.load('playerImages/Front - Idle_001.png')
frontIdle_002 = pygame.image.load('playerImages/Front - Idle_002.png')
frontIdle_003 = pygame.image.load('playerImages/Front - Idle_003.png')
frontIdle_004 = pygame.image.load('playerImages/Front - Idle_004.png')
frontIdle_005 = pygame.image.load('playerImages/Front - Idle_005.png')
frontIdle_006 = pygame.image.load('playerImages/Front - Idle_006.png')
frontIdle_007 = pygame.image.load('playerImages/Front - Idle_007.png')
frontIdle_008 = pygame.image.load('playerImages/Front - Idle_008.png')
frontIdle_009 = pygame.image.load('playerImages/Front - Idle_009.png')
frontIdle_010 = pygame.image.load('playerImages/Front - Idle_010.png')
frontIdle_011 = pygame.image.load('playerImages/Front - Idle_011.png')
frontIdle_012 = pygame.image.load('playerImages/Front - Idle_012.png')
frontIdle_013 = pygame.image.load('playerImages/Front - Idle_013.png')
frontIdle_014 = pygame.image.load('playerImages/Front - Idle_014.png')
frontIdle_015 = pygame.image.load('playerImages/Front - Idle_015.png')
frontIdle_016 = pygame.image.load('playerImages/Front - Idle_016.png')
frontIdle_017 = pygame.image.load('playerImages/Front - Idle_017.png')

frontWalking_000 = pygame.image.load('playerImages/Front - Walking_000.png')
frontWalking_001 = pygame.image.load('playerImages/Front - Walking_001.png')
frontWalking_002 = pygame.image.load('playerImages/Front - Walking_002.png')
frontWalking_003 = pygame.image.load('playerImages/Front - Walking_003.png')
frontWalking_004 = pygame.image.load('playerImages/Front - Walking_004.png')
frontWalking_005 = pygame.image.load('playerImages/Front - Walking_005.png')
frontWalking_006 = pygame.image.load('playerImages/Front - Walking_006.png')
frontWalking_007 = pygame.image.load('playerImages/Front - Walking_007.png')
frontWalking_008 = pygame.image.load('playerImages/Front - Walking_008.png')
frontWalking_009 = pygame.image.load('playerImages/Front - Walking_009.png')
frontWalking_010 = pygame.image.load('playerImages/Front - Walking_010.png')
frontWalking_011 = pygame.image.load('playerImages/Front - Walking_011.png')
frontWalking_012 = pygame.image.load('playerImages/Front - Walking_012.png')
frontWalking_013 = pygame.image.load('playerImages/Front - Walking_013.png')
frontWalking_014 = pygame.image.load('playerImages/Front - Walking_014.png')
frontWalking_015 = pygame.image.load('playerImages/Front - Walking_015.png')
frontWalking_016 = pygame.image.load('playerImages/Front - Walking_016.png')
frontWalking_017 = pygame.image.load('playerImages/Front - Walking_017.png')

frontSlashing_000 = pygame.image.load('playerImages/Front - Slashing_000.png')
frontSlashing_001 = pygame.image.load('playerImages/Front - Slashing_001.png')
frontSlashing_002 = pygame.image.load('playerImages/Front - Slashing_002.png')
frontSlashing_003 = pygame.image.load('playerImages/Front - Slashing_003.png')
frontSlashing_004 = pygame.image.load('playerImages/Front - Slashing_004.png')
frontSlashing_005 = pygame.image.load('playerImages/Front - Slashing_005.png')
frontSlashing_006 = pygame.image.load('playerImages/Front - Slashing_006.png')
frontSlashing_007 = pygame.image.load('playerImages/Front - Slashing_007.png')
frontSlashing_008 = pygame.image.load('playerImages/Front - Slashing_008.png')

rightIdle_000 = pygame.image.load('playerImages/Right - Idle_000.png')
rightIdle_001 = pygame.image.load('playerImages/Right - Idle_001.png')
rightIdle_002 = pygame.image.load('playerImages/Right - Idle_002.png')
rightIdle_003 = pygame.image.load('playerImages/Right - Idle_003.png')
rightIdle_004 = pygame.image.load('playerImages/Right - Idle_004.png')
rightIdle_005 = pygame.image.load('playerImages/Right - Idle_005.png')
rightIdle_006 = pygame.image.load('playerImages/Right - Idle_006.png')
rightIdle_007 = pygame.image.load('playerImages/Right - Idle_007.png')
rightIdle_008 = pygame.image.load('playerImages/Right - Idle_008.png')
rightIdle_009 = pygame.image.load('playerImages/Right - Idle_009.png')
rightIdle_010 = pygame.image.load('playerImages/Right - Idle_010.png')
rightIdle_011 = pygame.image.load('playerImages/Right - Idle_011.png')
rightIdle_012 = pygame.image.load('playerImages/Right - Idle_012.png')
rightIdle_013 = pygame.image.load('playerImages/Right - Idle_013.png')
rightIdle_014 = pygame.image.load('playerImages/Right - Idle_014.png')
rightIdle_015 = pygame.image.load('playerImages/Right - Idle_015.png')
rightIdle_016 = pygame.image.load('playerImages/Right - Idle_016.png')
rightIdle_017 = pygame.image.load('playerImages/Right - Idle_017.png')

rightWalking_000 = pygame.image.load('playerImages/Right - Walking_000.png')
rightWalking_001 = pygame.image.load('playerImages/Right - Walking_001.png')
rightWalking_002 = pygame.image.load('playerImages/Right - Walking_002.png')
rightWalking_003 = pygame.image.load('playerImages/Right - Walking_003.png')
rightWalking_004 = pygame.image.load('playerImages/Right - Walking_004.png')
rightWalking_005 = pygame.image.load('playerImages/Right - Walking_005.png')
rightWalking_006 = pygame.image.load('playerImages/Right - Walking_006.png')
rightWalking_007 = pygame.image.load('playerImages/Right - Walking_007.png')
rightWalking_008 = pygame.image.load('playerImages/Right - Walking_008.png')
rightWalking_009 = pygame.image.load('playerImages/Right - Walking_009.png')
rightWalking_010 = pygame.image.load('playerImages/Right - Walking_010.png')
rightWalking_011 = pygame.image.load('playerImages/Right - Walking_011.png')
rightWalking_012 = pygame.image.load('playerImages/Right - Walking_012.png')
rightWalking_013 = pygame.image.load('playerImages/Right - Walking_013.png')
rightWalking_014 = pygame.image.load('playerImages/Right - Walking_014.png')
rightWalking_015 = pygame.image.load('playerImages/Right - Walking_015.png')
rightWalking_016 = pygame.image.load('playerImages/Right - Walking_016.png')
rightWalking_017 = pygame.image.load('playerImages/Right - Walking_017.png')

rightSlashing_000 = pygame.image.load('playerImages/Right - Slashing_000.png')
rightSlashing_001 = pygame.image.load('playerImages/Right - Slashing_001.png')
rightSlashing_002 = pygame.image.load('playerImages/Right - Slashing_002.png')
rightSlashing_003 = pygame.image.load('playerImages/Right - Slashing_003.png')
rightSlashing_004 = pygame.image.load('playerImages/Right - Slashing_004.png')
rightSlashing_005 = pygame.image.load('playerImages/Right - Slashing_005.png')
rightSlashing_006 = pygame.image.load('playerImages/Right - Slashing_006.png')
rightSlashing_007 = pygame.image.load('playerImages/Right - Slashing_007.png')
rightSlashing_008 = pygame.image.load('playerImages/Right - Slashing_008.png')

backIdle_000 = pygame.image.load('playerImages/Back - Idle_000.png')
backIdle_001 = pygame.image.load('playerImages/Back - Idle_001.png')
backIdle_002 = pygame.image.load('playerImages/Back - Idle_002.png')
backIdle_003 = pygame.image.load('playerImages/Back - Idle_003.png')
backIdle_004 = pygame.image.load('playerImages/Back - Idle_004.png')
backIdle_005 = pygame.image.load('playerImages/Back - Idle_005.png')
backIdle_006 = pygame.image.load('playerImages/Back - Idle_006.png')
backIdle_007 = pygame.image.load('playerImages/Back - Idle_007.png')
backIdle_008 = pygame.image.load('playerImages/Back - Idle_008.png')
backIdle_009 = pygame.image.load('playerImages/Back - Idle_009.png')
backIdle_010 = pygame.image.load('playerImages/Back - Idle_010.png')
backIdle_011 = pygame.image.load('playerImages/Back - Idle_011.png')
backIdle_012 = pygame.image.load('playerImages/Back - Idle_012.png')
backIdle_013 = pygame.image.load('playerImages/Back - Idle_013.png')
backIdle_014 = pygame.image.load('playerImages/Back - Idle_014.png')
backIdle_015 = pygame.image.load('playerImages/Back - Idle_015.png')
backIdle_016 = pygame.image.load('playerImages/Back - Idle_016.png')
backIdle_017 = pygame.image.load('playerImages/Back - Idle_017.png')

SbackWalking_000 = pygame.image.load('playerImages/Back - Walking_000.png')
SbackWalking_001 = pygame.image.load('playerImages/Back - Walking_001.png')
SbackWalking_002 = pygame.image.load('playerImages/Back - Walking_002.png')
SbackWalking_003 = pygame.image.load('playerImages/Back - Walking_003.png')
SbackWalking_004 = pygame.image.load('playerImages/Back - Walking_004.png')
SbackWalking_005 = pygame.image.load('playerImages/Back - Walking_005.png')
SbackWalking_006 = pygame.image.load('playerImages/Back - Walking_006.png')
SbackWalking_007 = pygame.image.load('playerImages/Back - Walking_007.png')
SbackWalking_008 = pygame.image.load('playerImages/Back - Walking_008.png')
SbackWalking_009 = pygame.image.load('playerImages/Back - Walking_009.png')
SbackWalking_010 = pygame.image.load('playerImages/Back - Walking_010.png')
SbackWalking_011 = pygame.image.load('playerImages/Back - Walking_011.png')
SbackWalking_012 = pygame.image.load('playerImages/Back - Walking_012.png')
SbackWalking_013 = pygame.image.load('playerImages/Back - Walking_013.png')
SbackWalking_014 = pygame.image.load('playerImages/Back - Walking_014.png')
SbackWalking_015 = pygame.image.load('playerImages/Back - Walking_015.png')
SbackWalking_016 = pygame.image.load('playerImages/Back - Walking_016.png')
SbackWalking_017 = pygame.image.load('playerImages/Back - Walking_017.png')

SbackSlashing_000 = pygame.image.load('playerImages/Back - Slashing_000.png')
SbackSlashing_001 = pygame.image.load('playerImages/Back - Slashing_001.png')
SbackSlashing_002 = pygame.image.load('playerImages/Back - Slashing_002.png')
SbackSlashing_003 = pygame.image.load('playerImages/Back - Slashing_003.png')
SbackSlashing_004 = pygame.image.load('playerImages/Back - Slashing_004.png')
SbackSlashing_005 = pygame.image.load('playerImages/Back - Slashing_005.png')
SbackSlashing_006 = pygame.image.load('playerImages/Back - Slashing_006.png')
SbackSlashing_007 = pygame.image.load('playerImages/Back - Slashing_007.png')
SbackSlashing_008 = pygame.image.load('playerImages/Back - Slashing_008.png')

leftIdle_000 = pygame.image.load('playerImages/Left - Idle_000.png')
leftIdle_001 = pygame.image.load('playerImages/Left - Idle_001.png')
leftIdle_002 = pygame.image.load('playerImages/Left - Idle_002.png')
leftIdle_003 = pygame.image.load('playerImages/Left - Idle_003.png')
leftIdle_004 = pygame.image.load('playerImages/Left - Idle_004.png')
leftIdle_005 = pygame.image.load('playerImages/Left - Idle_005.png')
leftIdle_006 = pygame.image.load('playerImages/Left - Idle_006.png')
leftIdle_007 = pygame.image.load('playerImages/Left - Idle_007.png')
leftIdle_008 = pygame.image.load('playerImages/Left - Idle_008.png')
leftIdle_009 = pygame.image.load('playerImages/Left - Idle_009.png')
leftIdle_010 = pygame.image.load('playerImages/Left - Idle_010.png')
leftIdle_011 = pygame.image.load('playerImages/Left - Idle_011.png')
leftIdle_012 = pygame.image.load('playerImages/Left - Idle_012.png')
leftIdle_013 = pygame.image.load('playerImages/Left - Idle_013.png')
leftIdle_014 = pygame.image.load('playerImages/Left - Idle_014.png')
leftIdle_015 = pygame.image.load('playerImages/Left - Idle_015.png')
leftIdle_016 = pygame.image.load('playerImages/Left - Idle_016.png')
leftIdle_017 = pygame.image.load('playerImages/Left - Idle_017.png')

SleftWalking_000 = pygame.image.load('playerImages/Left - Walking_000.png')
SleftWalking_001 = pygame.image.load('playerImages/Left - Walking_001.png')
SleftWalking_002 = pygame.image.load('playerImages/Left - Walking_002.png')
SleftWalking_003 = pygame.image.load('playerImages/Left - Walking_003.png')
SleftWalking_004 = pygame.image.load('playerImages/Left - Walking_004.png')
SleftWalking_005 = pygame.image.load('playerImages/Left - Walking_005.png')
SleftWalking_006 = pygame.image.load('playerImages/Left - Walking_006.png')
SleftWalking_007 = pygame.image.load('playerImages/Left - Walking_007.png')
SleftWalking_008 = pygame.image.load('playerImages/Left - Walking_008.png')
SleftWalking_009 = pygame.image.load('playerImages/Left - Walking_009.png')
SleftWalking_010 = pygame.image.load('playerImages/Left - Walking_010.png')
SleftWalking_011 = pygame.image.load('playerImages/Left - Walking_011.png')
SleftWalking_012 = pygame.image.load('playerImages/Left - Walking_012.png')
SleftWalking_013 = pygame.image.load('playerImages/Left - Walking_013.png')
SleftWalking_014 = pygame.image.load('playerImages/Left - Walking_014.png')
SleftWalking_015 = pygame.image.load('playerImages/Left - Walking_015.png')
SleftWalking_016 = pygame.image.load('playerImages/Left - Walking_016.png')
SleftWalking_017 = pygame.image.load('playerImages/Left - Walking_017.png')

leftSlashing_000 = pygame.image.load('playerImages/Left - Slashing_000.png')
leftSlashing_001 = pygame.image.load('playerImages/Left - Slashing_001.png')
leftSlashing_002 = pygame.image.load('playerImages/Left - Slashing_002.png')
leftSlashing_003 = pygame.image.load('playerImages/Left - Slashing_003.png')
leftSlashing_004 = pygame.image.load('playerImages/Left - Slashing_004.png')
leftSlashing_005 = pygame.image.load('playerImages/Left - Slashing_005.png')
leftSlashing_006 = pygame.image.load('playerImages/Left - Slashing_006.png')
leftSlashing_007 = pygame.image.load('playerImages/Left - Slashing_007.png')
leftSlashing_008 = pygame.image.load('playerImages/Left - Slashing_008.png')
##########################################################################################

#SKELETON
SfrontIdle_000 = pygame.image.load('skeletonImages/Front - Idle_000.png')
SfrontIdle_001 = pygame.image.load('skeletonImages/Front - Idle_001.png')
SfrontIdle_002 = pygame.image.load('skeletonImages/Front - Idle_002.png')
SfrontIdle_003 = pygame.image.load('skeletonImages/Front - Idle_003.png')
SfrontIdle_004 = pygame.image.load('skeletonImages/Front - Idle_004.png')
SfrontIdle_005 = pygame.image.load('skeletonImages/Front - Idle_005.png')
SfrontIdle_006 = pygame.image.load('skeletonImages/Front - Idle_006.png')
SfrontIdle_007 = pygame.image.load('skeletonImages/Front - Idle_007.png')
SfrontIdle_008 = pygame.image.load('skeletonImages/Front - Idle_008.png')
SfrontIdle_009 = pygame.image.load('skeletonImages/Front - Idle_009.png')
SfrontIdle_010 = pygame.image.load('skeletonImages/Front - Idle_010.png')
SfrontIdle_011 = pygame.image.load('skeletonImages/Front - Idle_011.png')
#SfrontIdle_012 = pygame.image.load('skeletonImages/Front - Idle_012.png')
#SfrontIdle_013 = pygame.image.load('skeletonImages/Front - Idle_013.png')
#SfrontIdle_014 = pygame.image.load('skeletonImages/Front - Idle_014.png')
#SfrontIdle_015 = pygame.image.load('skeletonImages/Front - Idle_015.png')
#SfrontIdle_016 = pygame.image.load('skeletonImages/Front - Idle_016.png')
#SfrontIdle_017 = pygame.image.load('skeletonImages/Front - Idle_017.png')

SfrontWalking_000 = pygame.image.load('skeletonImages/Front - Walking_000.png')
SfrontWalking_001 = pygame.image.load('skeletonImages/Front - Walking_001.png')
SfrontWalking_002 = pygame.image.load('skeletonImages/Front - Walking_002.png')
SfrontWalking_003 = pygame.image.load('skeletonImages/Front - Walking_003.png')
SfrontWalking_004 = pygame.image.load('skeletonImages/Front - Walking_004.png')
SfrontWalking_005 = pygame.image.load('skeletonImages/Front - Walking_005.png')
SfrontWalking_006 = pygame.image.load('skeletonImages/Front - Walking_006.png')
SfrontWalking_007 = pygame.image.load('skeletonImages/Front - Walking_007.png')
SfrontWalking_008 = pygame.image.load('skeletonImages/Front - Walking_008.png')
SfrontWalking_009 = pygame.image.load('skeletonImages/Front - Walking_009.png')
SfrontWalking_010 = pygame.image.load('skeletonImages/Front - Walking_010.png')
SfrontWalking_011 = pygame.image.load('skeletonImages/Front - Walking_011.png')
SfrontWalking_012 = pygame.image.load('skeletonImages/Front - Walking_012.png')
SfrontWalking_013 = pygame.image.load('skeletonImages/Front - Walking_013.png')
SfrontWalking_014 = pygame.image.load('skeletonImages/Front - Walking_014.png')
SfrontWalking_015 = pygame.image.load('skeletonImages/Front - Walking_015.png')
SfrontWalking_016 = pygame.image.load('skeletonImages/Front - Walking_016.png')
SfrontWalking_017 = pygame.image.load('skeletonImages/Front - Walking_017.png')

SfrontSlashing_000 = pygame.image.load('skeletonImages/Front - Slashing_000.png')
SfrontSlashing_001 = pygame.image.load('skeletonImages/Front - Slashing_001.png')
SfrontSlashing_002 = pygame.image.load('skeletonImages/Front - Slashing_002.png')
SfrontSlashing_003 = pygame.image.load('skeletonImages/Front - Slashing_003.png')
SfrontSlashing_004 = pygame.image.load('skeletonImages/Front - Slashing_004.png')
SfrontSlashing_005 = pygame.image.load('skeletonImages/Front - Slashing_005.png')
SfrontSlashing_006 = pygame.image.load('skeletonImages/Front - Slashing_006.png')
SfrontSlashing_007 = pygame.image.load('skeletonImages/Front - Slashing_007.png')
SfrontSlashing_008 = pygame.image.load('skeletonImages/Front - Slashing_008.png')

SrightIdle_000 = pygame.image.load('skeletonImages/Right - Idle_000.png')
SrightIdle_001 = pygame.image.load('skeletonImages/Right - Idle_001.png')
SrightIdle_002 = pygame.image.load('skeletonImages/Right - Idle_002.png')
SrightIdle_003 = pygame.image.load('skeletonImages/Right - Idle_003.png')
SrightIdle_004 = pygame.image.load('skeletonImages/Right - Idle_004.png')
SrightIdle_005 = pygame.image.load('skeletonImages/Right - Idle_005.png')
SrightIdle_006 = pygame.image.load('skeletonImages/Right - Idle_006.png')
SrightIdle_007 = pygame.image.load('skeletonImages/Right - Idle_007.png')
SrightIdle_008 = pygame.image.load('skeletonImages/Right - Idle_008.png')
SrightIdle_009 = pygame.image.load('skeletonImages/Right - Idle_009.png')
SrightIdle_010 = pygame.image.load('skeletonImages/Right - Idle_010.png')
SrightIdle_011 = pygame.image.load('skeletonImages/Right - Idle_011.png')
#SrightIdle_012 = pygame.image.load('skeletonImages/Right - Idle_012.png')
#SrightIdle_013 = pygame.image.load('skeletonImages/Right - Idle_013.png')
#SrightIdle_014 = pygame.image.load('skeletonImages/Right - Idle_014.png')
#SrightIdle_015 = pygame.image.load('skeletonImages/Right - Idle_015.png')
#SrightIdle_016 = pygame.image.load('skeletonImages/Right - Idle_016.png')
#SrightIdle_017 = pygame.image.load('skeletonImages/Right - Idle_017.png')

SrightWalking_000 = pygame.image.load('skeletonImages/Right - Walking_000.png')
SrightWalking_001 = pygame.image.load('skeletonImages/Right - Walking_001.png')
SrightWalking_002 = pygame.image.load('skeletonImages/Right - Walking_002.png')
SrightWalking_003 = pygame.image.load('skeletonImages/Right - Walking_003.png')
SrightWalking_004 = pygame.image.load('skeletonImages/Right - Walking_004.png')
SrightWalking_005 = pygame.image.load('skeletonImages/Right - Walking_005.png')
SrightWalking_006 = pygame.image.load('skeletonImages/Right - Walking_006.png')
SrightWalking_007 = pygame.image.load('skeletonImages/Right - Walking_007.png')
SrightWalking_008 = pygame.image.load('skeletonImages/Right - Walking_008.png')
SrightWalking_009 = pygame.image.load('skeletonImages/Right - Walking_009.png')
SrightWalking_010 = pygame.image.load('skeletonImages/Right - Walking_010.png')
SrightWalking_011 = pygame.image.load('skeletonImages/Right - Walking_011.png')
SrightWalking_012 = pygame.image.load('skeletonImages/Right - Walking_012.png')
SrightWalking_013 = pygame.image.load('skeletonImages/Right - Walking_013.png')
SrightWalking_014 = pygame.image.load('skeletonImages/Right - Walking_014.png')
SrightWalking_015 = pygame.image.load('skeletonImages/Right - Walking_015.png')
SrightWalking_016 = pygame.image.load('skeletonImages/Right - Walking_016.png')
SrightWalking_017 = pygame.image.load('skeletonImages/Right - Walking_017.png')

SrightSlashing_000 = pygame.image.load('skeletonImages/Right - Slashing_000.png')
SrightSlashing_001 = pygame.image.load('skeletonImages/Right - Slashing_001.png')
SrightSlashing_002 = pygame.image.load('skeletonImages/Right - Slashing_002.png')
SrightSlashing_003 = pygame.image.load('skeletonImages/Right - Slashing_003.png')
SrightSlashing_004 = pygame.image.load('skeletonImages/Right - Slashing_004.png')
SrightSlashing_005 = pygame.image.load('skeletonImages/Right - Slashing_005.png')
SrightSlashing_006 = pygame.image.load('skeletonImages/Right - Slashing_006.png')
SrightSlashing_007 = pygame.image.load('skeletonImages/Right - Slashing_007.png')
SrightSlashing_008 = pygame.image.load('skeletonImages/Right - Slashing_008.png')

SbackIdle_000 = pygame.image.load('skeletonImages/Back - Idle_000.png')
SbackIdle_001 = pygame.image.load('skeletonImages/Back - Idle_001.png')
SbackIdle_002 = pygame.image.load('skeletonImages/Back - Idle_002.png')
SbackIdle_003 = pygame.image.load('skeletonImages/Back - Idle_003.png')
SbackIdle_004 = pygame.image.load('skeletonImages/Back - Idle_004.png')
SbackIdle_005 = pygame.image.load('skeletonImages/Back - Idle_005.png')
SbackIdle_006 = pygame.image.load('skeletonImages/Back - Idle_006.png')
SbackIdle_007 = pygame.image.load('skeletonImages/Back - Idle_007.png')
SbackIdle_008 = pygame.image.load('skeletonImages/Back - Idle_008.png')
SbackIdle_009 = pygame.image.load('skeletonImages/Back - Idle_009.png')
SbackIdle_010 = pygame.image.load('skeletonImages/Back - Idle_010.png')
SbackIdle_011 = pygame.image.load('skeletonImages/Back - Idle_011.png')
#SbackIdle_012 = pygame.image.load('skeletonImages/Back - Idle_012.png')
#SbackIdle_013 = pygame.image.load('skeletonImages/Back - Idle_013.png')
#SbackIdle_014 = pygame.image.load('skeletonImages/Back - Idle_014.png')
#SbackIdle_015 = pygame.image.load('skeletonImages/Back - Idle_015.png')
#SbackIdle_016 = pygame.image.load('skeletonImages/Back - Idle_016.png')
#SbackIdle_017 = pygame.image.load('skeletonImages/Back - Idle_017.png')

SSbackWalking_000 = pygame.image.load('skeletonImages/Back - Walking_000.png')
SSbackWalking_001 = pygame.image.load('skeletonImages/Back - Walking_001.png')
SSbackWalking_002 = pygame.image.load('skeletonImages/Back - Walking_002.png')
SSbackWalking_003 = pygame.image.load('skeletonImages/Back - Walking_003.png')
SSbackWalking_004 = pygame.image.load('skeletonImages/Back - Walking_004.png')
SSbackWalking_005 = pygame.image.load('skeletonImages/Back - Walking_005.png')
SSbackWalking_006 = pygame.image.load('skeletonImages/Back - Walking_006.png')
SSbackWalking_007 = pygame.image.load('skeletonImages/Back - Walking_007.png')
SSbackWalking_008 = pygame.image.load('skeletonImages/Back - Walking_008.png')
SSbackWalking_009 = pygame.image.load('skeletonImages/Back - Walking_009.png')
SSbackWalking_010 = pygame.image.load('skeletonImages/Back - Walking_010.png')
SSbackWalking_011 = pygame.image.load('skeletonImages/Back - Walking_011.png')
SSbackWalking_012 = pygame.image.load('skeletonImages/Back - Walking_012.png')
SSbackWalking_013 = pygame.image.load('skeletonImages/Back - Walking_013.png')
SSbackWalking_014 = pygame.image.load('skeletonImages/Back - Walking_014.png')
SSbackWalking_015 = pygame.image.load('skeletonImages/Back - Walking_015.png')
SSbackWalking_016 = pygame.image.load('skeletonImages/Back - Walking_016.png')
SSbackWalking_017 = pygame.image.load('skeletonImages/Back - Walking_017.png')

SSbackSlashing_000 = pygame.image.load('skeletonImages/Back - Slashing_000.png')
SSbackSlashing_001 = pygame.image.load('skeletonImages/Back - Slashing_001.png')
SSbackSlashing_002 = pygame.image.load('skeletonImages/Back - Slashing_002.png')
SSbackSlashing_003 = pygame.image.load('skeletonImages/Back - Slashing_003.png')
SSbackSlashing_004 = pygame.image.load('skeletonImages/Back - Slashing_004.png')
SSbackSlashing_005 = pygame.image.load('skeletonImages/Back - Slashing_005.png')
SSbackSlashing_006 = pygame.image.load('skeletonImages/Back - Slashing_006.png')
SSbackSlashing_007 = pygame.image.load('skeletonImages/Back - Slashing_007.png')
SSbackSlashing_008 = pygame.image.load('skeletonImages/Back - Slashing_008.png')

SleftIdle_000 = pygame.image.load('skeletonImages/Left - Idle_000.png')
SleftIdle_001 = pygame.image.load('skeletonImages/Left - Idle_001.png')
SleftIdle_002 = pygame.image.load('skeletonImages/Left - Idle_002.png')
SleftIdle_003 = pygame.image.load('skeletonImages/Left - Idle_003.png')
SleftIdle_004 = pygame.image.load('skeletonImages/Left - Idle_004.png')
SleftIdle_005 = pygame.image.load('skeletonImages/Left - Idle_005.png')
SleftIdle_006 = pygame.image.load('skeletonImages/Left - Idle_006.png')
SleftIdle_007 = pygame.image.load('skeletonImages/Left - Idle_007.png')
SleftIdle_008 = pygame.image.load('skeletonImages/Left - Idle_008.png')
SleftIdle_009 = pygame.image.load('skeletonImages/Left - Idle_009.png')
SleftIdle_010 = pygame.image.load('skeletonImages/Left - Idle_010.png')
SleftIdle_011 = pygame.image.load('skeletonImages/Left - Idle_011.png')
#SleftIdle_012 = pygame.image.load('skeletonImages/Left - Idle_012.png')
#SleftIdle_013 = pygame.image.load('skeletonImages/Left - Idle_013.png')
#SleftIdle_014 = pygame.image.load('skeletonImages/Left - Idle_014.png')
#SleftIdle_015 = pygame.image.load('skeletonImages/Left - Idle_015.png')
#SleftIdle_016 = pygame.image.load('skeletonImages/Left - Idle_016.png')
#SleftIdle_017 = pygame.image.load('skeletonImages/Left - Idle_017.png')

SSleftWalking_000 = pygame.image.load('skeletonImages/Left - Walking_000.png')
SSleftWalking_001 = pygame.image.load('skeletonImages/Left - Walking_001.png')
SSleftWalking_002 = pygame.image.load('skeletonImages/Left - Walking_002.png')
SSleftWalking_003 = pygame.image.load('skeletonImages/Left - Walking_003.png')
SSleftWalking_004 = pygame.image.load('skeletonImages/Left - Walking_004.png')
SSleftWalking_005 = pygame.image.load('skeletonImages/Left - Walking_005.png')
SSleftWalking_006 = pygame.image.load('skeletonImages/Left - Walking_006.png')
SSleftWalking_007 = pygame.image.load('skeletonImages/Left - Walking_007.png')
SSleftWalking_008 = pygame.image.load('skeletonImages/Left - Walking_008.png')
SSleftWalking_009 = pygame.image.load('skeletonImages/Left - Walking_009.png')
SSleftWalking_010 = pygame.image.load('skeletonImages/Left - Walking_010.png')
SSleftWalking_011 = pygame.image.load('skeletonImages/Left - Walking_011.png')
SSleftWalking_012 = pygame.image.load('skeletonImages/Left - Walking_012.png')
SSleftWalking_013 = pygame.image.load('skeletonImages/Left - Walking_013.png')
SSleftWalking_014 = pygame.image.load('skeletonImages/Left - Walking_014.png')
SSleftWalking_015 = pygame.image.load('skeletonImages/Left - Walking_015.png')
SSleftWalking_016 = pygame.image.load('skeletonImages/Left - Walking_016.png')
SSleftWalking_017 = pygame.image.load('skeletonImages/Left - Walking_017.png')

SleftSlashing_000 = pygame.image.load('skeletonImages/Left - Slashing_000.png')
SleftSlashing_001 = pygame.image.load('skeletonImages/Left - Slashing_001.png')
SleftSlashing_002 = pygame.image.load('skeletonImages/Left - Slashing_002.png')
SleftSlashing_003 = pygame.image.load('skeletonImages/Left - Slashing_003.png')
SleftSlashing_004 = pygame.image.load('skeletonImages/Left - Slashing_004.png')
SleftSlashing_005 = pygame.image.load('skeletonImages/Left - Slashing_005.png')
SleftSlashing_006 = pygame.image.load('skeletonImages/Left - Slashing_006.png')
SleftSlashing_007 = pygame.image.load('skeletonImages/Left - Slashing_007.png')
SleftSlashing_008 = pygame.image.load('skeletonImages/Left - Slashing_008.png')

##########################################################################################
class Player:
    def __init__(self):

        self.animateCounter = 0
        self.animate = 0
        self.direction = 0
        self.attackDelay = 10

        self.walkCounter = 0
        self.attackCounter = 0

        self.x = (64 * 3 )-32
        self.y = 64
        self.Tile = self.Tile = int(((self.x - 32 + 64) /64) + (((self.y + 64)/ 64) * 10)) #23
        self.attackedTile = 100 #out of map

        self.rightBorder = [9,19,29,39,49,59,69]
        self.leftBorder =  [ 0,10,20,30,40,50,60]
        self.backBorder =  [0,1,2,3,4,5,6,7,8,9]
        self.frontBorder = [60,61,62,63,64,65,66,67,68,69]

    def draw(self):

        #print(self.Tile, self.attackedTile)
        if self.direction == 0: #Front

            if self.animate == 0: #front Idle
                if int(self.animateCounter) == 0: screen.blit(frontIdle_000,(self.x,self.y))
                elif int(self.animateCounter) == 1: screen.blit(frontIdle_001,(self.x,self.y))
                elif int(self.animateCounter) == 2: screen.blit(frontIdle_002,(self.x,self.y))
                elif int(self.animateCounter) == 3: screen.blit(frontIdle_003,(self.x,self.y))
                elif int(self.animateCounter) == 4: screen.blit(frontIdle_004,(self.x,self.y))
                elif int(self.animateCounter) == 5: screen.blit(frontIdle_005,(self.x,self.y))
                elif int(self.animateCounter) == 6: screen.blit(frontIdle_006,(self.x,self.y))
                elif int(self.animateCounter) == 7: screen.blit(frontIdle_007,(self.x,self.y))
                elif int(self.animateCounter) == 8: screen.blit(frontIdle_008,(self.x,self.y))
                elif int(self.animateCounter) == 9: screen.blit(frontIdle_009,(self.x,self.y))
                elif int(self.animateCounter) == 10: screen.blit(frontIdle_010,(self.x,self.y))
                elif int(self.animateCounter) == 11: screen.blit(frontIdle_011,(self.x,self.y))
                elif int(self.animateCounter) == 12: screen.blit(frontIdle_012,(self.x,self.y))
                elif int(self.animateCounter) == 13: screen.blit(frontIdle_013,(self.x,self.y))
                elif int(self.animateCounter) == 14: screen.blit(frontIdle_014,(self.x,self.y))
                elif int(self.animateCounter) == 15: screen.blit(frontIdle_015,(self.x,self.y))
                elif int(self.animateCounter) == 16: screen.blit(frontIdle_016,(self.x,self.y))
                elif int(self.animateCounter) == 17: screen.blit(frontIdle_017,(self.x,self.y))

            elif self.animate == 1: #front Walking
                if int(self.animateCounter) == 0: screen.blit(frontWalking_000,(self.x,self.y))
                elif int(self.animateCounter) == 1: screen.blit(frontWalking_001,(self.x,self.y))
                elif int(self.animateCounter) == 2: screen.blit(frontWalking_002,(self.x,self.y))
                elif int(self.animateCounter) == 3: screen.blit(frontWalking_003,(self.x,self.y))
                elif int(self.animateCounter) == 4: screen.blit(frontWalking_004,(self.x,self.y))
                elif int(self.animateCounter) == 5: screen.blit(frontWalking_005,(self.x,self.y))
                elif int(self.animateCounter) == 6: screen.blit(frontWalking_006,(self.x,self.y))
                elif int(self.animateCounter) == 7: screen.blit(frontWalking_007,(self.x,self.y))
                elif int(self.animateCounter) == 8: screen.blit(frontWalking_008,(self.x,self.y))
                elif int(self.animateCounter) == 9: screen.blit(frontWalking_009,(self.x,self.y))
                elif int(self.animateCounter) == 10: screen.blit(frontWalking_010,(self.x,self.y))
                elif int(self.animateCounter) == 11: screen.blit(frontWalking_011,(self.x,self.y))
                elif int(self.animateCounter) == 12: screen.blit(frontWalking_012,(self.x,self.y))
                elif int(self.animateCounter) == 13: screen.blit(frontWalking_013,(self.x,self.y))
                elif int(self.animateCounter) == 14: screen.blit(frontWalking_014,(self.x,self.y))
                elif int(self.animateCounter) == 15: screen.blit(frontWalking_015,(self.x,self.y))
                elif int(self.animateCounter) == 16: screen.blit(frontWalking_016,(self.x,self.y))
                elif int(self.animateCounter) == 17: screen.blit(frontWalking_017,(self.x,self.y))

            elif self.animate == 2:#front Attack
                if int(self.animateCounter) == 0: screen.blit(frontSlashing_000,(self.x,self.y))
                elif int(self.animateCounter) == 1: screen.blit(frontSlashing_001,(self.x,self.y))
                elif int(self.animateCounter) == 2: screen.blit(frontSlashing_002,(self.x,self.y))
                elif int(self.animateCounter) == 3: screen.blit(frontSlashing_003,(self.x,self.y))
                elif int(self.animateCounter) == 4: screen.blit(frontSlashing_004,(self.x,self.y))
                elif int(self.animateCounter) == 5: screen.blit(frontSlashing_005,(self.x,self.y))
                elif int(self.animateCounter) == 6: screen.blit(frontSlashing_006,(self.x,self.y))
                elif int(self.animateCounter) == 7: screen.blit(frontSlashing_007,(self.x,self.y))
                elif int(self.animateCounter) == 8: screen.blit(frontSlashing_008,(self.x,self.y))

                if self.Tile not in self.frontBorder:
                    self.attackedTile = self.Tile + 10
    

        elif self.direction == 1: #Right

            if self.animate == 0: #right Idle
                if int(self.animateCounter) == 0: screen.blit(rightIdle_000,(self.x,self.y))
                elif int(self.animateCounter) == 1: screen.blit(rightIdle_001,(self.x,self.y))
                elif int(self.animateCounter) == 2: screen.blit(rightIdle_002,(self.x,self.y))
                elif int(self.animateCounter) == 3: screen.blit(rightIdle_003,(self.x,self.y))
                elif int(self.animateCounter) == 4: screen.blit(rightIdle_004,(self.x,self.y))
                elif int(self.animateCounter) == 5: screen.blit(rightIdle_005,(self.x,self.y))
                elif int(self.animateCounter) == 6: screen.blit(rightIdle_006,(self.x,self.y))
                elif int(self.animateCounter) == 7: screen.blit(rightIdle_007,(self.x,self.y))
                elif int(self.animateCounter) == 8: screen.blit(rightIdle_008,(self.x,self.y))
                elif int(self.animateCounter) == 9: screen.blit(rightIdle_009,(self.x,self.y))
                elif int(self.animateCounter) == 10: screen.blit(rightIdle_010,(self.x,self.y))
                elif int(self.animateCounter) == 11: screen.blit(rightIdle_011,(self.x,self.y))
                elif int(self.animateCounter) == 12: screen.blit(rightIdle_012,(self.x,self.y))
                elif int(self.animateCounter) == 13: screen.blit(rightIdle_013,(self.x,self.y))
                elif int(self.animateCounter) == 14: screen.blit(rightIdle_014,(self.x,self.y))
                elif int(self.animateCounter) == 15: screen.blit(rightIdle_015,(self.x,self.y))
                elif int(self.animateCounter) == 16: screen.blit(rightIdle_016,(self.x,self.y))
                elif int(self.animateCounter) == 17: screen.blit(rightIdle_017,(self.x,self.y))

            elif self.animate == 1: #right Walking
                if int(self.animateCounter) == 0: screen.blit(rightWalking_000,(self.x,self.y))
                elif int(self.animateCounter) == 1: screen.blit(rightWalking_001,(self.x,self.y))
                elif int(self.animateCounter) == 2: screen.blit(rightWalking_002,(self.x,self.y))
                elif int(self.animateCounter) == 3: screen.blit(rightWalking_003,(self.x,self.y))
                elif int(self.animateCounter) == 4: screen.blit(rightWalking_004,(self.x,self.y))
                elif int(self.animateCounter) == 5: screen.blit(rightWalking_005,(self.x,self.y))
                elif int(self.animateCounter) == 6: screen.blit(rightWalking_006,(self.x,self.y))
                elif int(self.animateCounter) == 7: screen.blit(rightWalking_007,(self.x,self.y))
                elif int(self.animateCounter) == 8: screen.blit(rightWalking_008,(self.x,self.y))
                elif int(self.animateCounter) == 9: screen.blit(rightWalking_009,(self.x,self.y))
                elif int(self.animateCounter) == 10: screen.blit(rightWalking_010,(self.x,self.y))
                elif int(self.animateCounter) == 11: screen.blit(rightWalking_011,(self.x,self.y))
                elif int(self.animateCounter) == 12: screen.blit(rightWalking_012,(self.x,self.y))
                elif int(self.animateCounter) == 13: screen.blit(rightWalking_013,(self.x,self.y))
                elif int(self.animateCounter) == 14: screen.blit(rightWalking_014,(self.x,self.y))
                elif int(self.animateCounter) == 15: screen.blit(rightWalking_015,(self.x,self.y))
                elif int(self.animateCounter) == 16: screen.blit(rightWalking_016,(self.x,self.y))
                elif int(self.animateCounter) == 17: screen.blit(rightWalking_017,(self.x,self.y))

            elif self.animate == 2:#right Attack
                if int(self.animateCounter) == 0: screen.blit(rightSlashing_000,(self.x,self.y))
                elif int(self.animateCounter) == 1: screen.blit(rightSlashing_001,(self.x,self.y))
                elif int(self.animateCounter) == 2: screen.blit(rightSlashing_002,(self.x,self.y))
                elif int(self.animateCounter) == 3: screen.blit(rightSlashing_003,(self.x,self.y))
                elif int(self.animateCounter) == 4: screen.blit(rightSlashing_004,(self.x,self.y))
                elif int(self.animateCounter) == 5: screen.blit(rightSlashing_005,(self.x,self.y))
                elif int(self.animateCounter) == 6: screen.blit(rightSlashing_006,(self.x,self.y))
                elif int(self.animateCounter) == 7: screen.blit(rightSlashing_007,(self.x,self.y))
                elif int(self.animateCounter) == 8: screen.blit(rightSlashing_008,(self.x,self.y))

                if self.Tile not in self.rightBorder:
                    self.attackedTile = self.Tile + 1

        elif self.direction == 2: #Back

            if self.animate == 0:#back Idle
                if int(self.animateCounter) == 0: screen.blit(backIdle_000,(self.x,self.y))
                elif int(self.animateCounter) == 1: screen.blit(backIdle_001,(self.x,self.y))
                elif int(self.animateCounter) == 2: screen.blit(backIdle_002,(self.x,self.y))
                elif int(self.animateCounter) == 3: screen.blit(backIdle_003,(self.x,self.y))
                elif int(self.animateCounter) == 4: screen.blit(backIdle_004,(self.x,self.y))
                elif int(self.animateCounter) == 5: screen.blit(backIdle_005,(self.x,self.y))
                elif int(self.animateCounter) == 6: screen.blit(backIdle_006,(self.x,self.y))
                elif int(self.animateCounter) == 7: screen.blit(backIdle_007,(self.x,self.y))
                elif int(self.animateCounter) == 8: screen.blit(backIdle_008,(self.x,self.y))
                elif int(self.animateCounter) == 9: screen.blit(backIdle_009,(self.x,self.y))
                elif int(self.animateCounter) == 10: screen.blit(backIdle_010,(self.x,self.y))
                elif int(self.animateCounter) == 11: screen.blit(backIdle_011,(self.x,self.y))
                elif int(self.animateCounter) == 12: screen.blit(backIdle_012,(self.x,self.y))
                elif int(self.animateCounter) == 13: screen.blit(backIdle_013,(self.x,self.y))
                elif int(self.animateCounter) == 14: screen.blit(backIdle_014,(self.x,self.y))
                elif int(self.animateCounter) == 15: screen.blit(backIdle_015,(self.x,self.y))
                elif int(self.animateCounter) == 16: screen.blit(backIdle_016,(self.x,self.y))
                elif int(self.animateCounter) == 17: screen.blit(backIdle_017,(self.x,self.y))


            elif self.animate == 1:#back Walking
                if int(self.animateCounter) == 0: screen.blit(SbackWalking_000,(self.x,self.y))
                elif int(self.animateCounter) == 1: screen.blit(SbackWalking_001,(self.x,self.y))
                elif int(self.animateCounter) == 2: screen.blit(SbackWalking_002,(self.x,self.y))
                elif int(self.animateCounter) == 3: screen.blit(SbackWalking_003,(self.x,self.y))
                elif int(self.animateCounter) == 4: screen.blit(SbackWalking_004,(self.x,self.y))
                elif int(self.animateCounter) == 5: screen.blit(SbackWalking_005,(self.x,self.y))
                elif int(self.animateCounter) == 6: screen.blit(SbackWalking_006,(self.x,self.y))
                elif int(self.animateCounter) == 7: screen.blit(SbackWalking_007,(self.x,self.y))
                elif int(self.animateCounter) == 8: screen.blit(SbackWalking_008,(self.x,self.y))
                elif int(self.animateCounter) == 9: screen.blit(SbackWalking_009,(self.x,self.y))
                elif int(self.animateCounter) == 10: screen.blit(SbackWalking_010,(self.x,self.y))
                elif int(self.animateCounter) == 11: screen.blit(SbackWalking_011,(self.x,self.y))
                elif int(self.animateCounter) == 12: screen.blit(SbackWalking_012,(self.x,self.y))
                elif int(self.animateCounter) == 13: screen.blit(SbackWalking_013,(self.x,self.y))
                elif int(self.animateCounter) == 14: screen.blit(SbackWalking_014,(self.x,self.y))
                elif int(self.animateCounter) == 15: screen.blit(SbackWalking_015,(self.x,self.y))
                elif int(self.animateCounter) == 16: screen.blit(SbackWalking_016,(self.x,self.y))
                elif int(self.animateCounter) == 17: screen.blit(SbackWalking_017,(self.x,self.y))

            elif self.animate == 2:#back Attack
                if int(self.animateCounter) == 0: screen.blit(SbackSlashing_000,(self.x,self.y))
                elif int(self.animateCounter) == 1: screen.blit(SbackSlashing_001,(self.x,self.y))
                elif int(self.animateCounter) == 2: screen.blit(SbackSlashing_002,(self.x,self.y))
                elif int(self.animateCounter) == 3: screen.blit(SbackSlashing_003,(self.x,self.y))
                elif int(self.animateCounter) == 4: screen.blit(SbackSlashing_004,(self.x,self.y))
                elif int(self.animateCounter) == 5: screen.blit(SbackSlashing_005,(self.x,self.y))
                elif int(self.animateCounter) == 6: screen.blit(SbackSlashing_006,(self.x,self.y))
                elif int(self.animateCounter) == 7: screen.blit(SbackSlashing_007,(self.x,self.y))
                elif int(self.animateCounter) == 8: screen.blit(SbackSlashing_008,(self.x,self.y))
                
                if self.Tile not in self.backBorder:
                    self.attackedTile = self.Tile - 10

        elif self.direction == 3: #Left

            if self.animate == 0: #left Idle
                if int(self.animateCounter) == 0: screen.blit(leftIdle_000,(self.x,self.y))
                elif int(self.animateCounter) == 1: screen.blit(leftIdle_001,(self.x,self.y))
                elif int(self.animateCounter) == 2: screen.blit(leftIdle_002,(self.x,self.y))
                elif int(self.animateCounter) == 3: screen.blit(leftIdle_003,(self.x,self.y))
                elif int(self.animateCounter) == 4: screen.blit(leftIdle_004,(self.x,self.y))
                elif int(self.animateCounter) == 5: screen.blit(leftIdle_005,(self.x,self.y))
                elif int(self.animateCounter) == 6: screen.blit(leftIdle_006,(self.x,self.y))
                elif int(self.animateCounter) == 7: screen.blit(leftIdle_007,(self.x,self.y))
                elif int(self.animateCounter) == 8: screen.blit(leftIdle_008,(self.x,self.y))
                elif int(self.animateCounter) == 9: screen.blit(leftIdle_009,(self.x,self.y))
                elif int(self.animateCounter) == 10: screen.blit(leftIdle_010,(self.x,self.y))
                elif int(self.animateCounter) == 11: screen.blit(leftIdle_011,(self.x,self.y))
                elif int(self.animateCounter) == 12: screen.blit(leftIdle_012,(self.x,self.y))
                elif int(self.animateCounter) == 13: screen.blit(leftIdle_013,(self.x,self.y))
                elif int(self.animateCounter) == 14: screen.blit(leftIdle_014,(self.x,self.y))
                elif int(self.animateCounter) == 15: screen.blit(leftIdle_015,(self.x,self.y))
                elif int(self.animateCounter) == 16: screen.blit(leftIdle_016,(self.x,self.y))
                elif int(self.animateCounter) == 17: screen.blit(leftIdle_017,(self.x,self.y))

            elif self.animate == 1: #left Walking
                if int(self.animateCounter) == 0: screen.blit(SleftWalking_000,(self.x,self.y))
                elif int(self.animateCounter) == 1: screen.blit(SleftWalking_001,(self.x,self.y))
                elif int(self.animateCounter) == 2: screen.blit(SleftWalking_002,(self.x,self.y))
                elif int(self.animateCounter) == 3: screen.blit(SleftWalking_003,(self.x,self.y))
                elif int(self.animateCounter) == 4: screen.blit(SleftWalking_004,(self.x,self.y))
                elif int(self.animateCounter) == 5: screen.blit(SleftWalking_005,(self.x,self.y))
                elif int(self.animateCounter) == 6: screen.blit(SleftWalking_006,(self.x,self.y))
                elif int(self.animateCounter) == 7: screen.blit(SleftWalking_007,(self.x,self.y))
                elif int(self.animateCounter) == 8: screen.blit(SleftWalking_008,(self.x,self.y))
                elif int(self.animateCounter) == 9: screen.blit(SleftWalking_009,(self.x,self.y))
                elif int(self.animateCounter) == 10: screen.blit(SleftWalking_010,(self.x,self.y))
                elif int(self.animateCounter) == 11: screen.blit(SleftWalking_011,(self.x,self.y))
                elif int(self.animateCounter) == 12: screen.blit(SleftWalking_012,(self.x,self.y))
                elif int(self.animateCounter) == 13: screen.blit(SleftWalking_013,(self.x,self.y))
                elif int(self.animateCounter) == 14: screen.blit(SleftWalking_014,(self.x,self.y))
                elif int(self.animateCounter) == 15: screen.blit(SleftWalking_015,(self.x,self.y))
                elif int(self.animateCounter) == 16: screen.blit(SleftWalking_016,(self.x,self.y))
                elif int(self.animateCounter) == 17: screen.blit(SleftWalking_017,(self.x,self.y))

            elif self.animate == 2:#left Attack
                if int(self.animateCounter) == 0: screen.blit(leftSlashing_000,(self.x,self.y))
                elif int(self.animateCounter) == 1: screen.blit(leftSlashing_001,(self.x,self.y))
                elif int(self.animateCounter) == 2: screen.blit(leftSlashing_002,(self.x,self.y))
                elif int(self.animateCounter) == 3: screen.blit(leftSlashing_003,(self.x,self.y))
                elif int(self.animateCounter) == 4: screen.blit(leftSlashing_004,(self.x,self.y))
                elif int(self.animateCounter) == 5: screen.blit(leftSlashing_005,(self.x,self.y))
                elif int(self.animateCounter) == 6: screen.blit(leftSlashing_006,(self.x,self.y))
                elif int(self.animateCounter) == 7: screen.blit(leftSlashing_007,(self.x,self.y))
                elif int(self.animateCounter) == 8: screen.blit(leftSlashing_008,(self.x,self.y))

                if self.Tile not in self.leftBorder:
                    self.attackedTile = self.Tile - 1


    def movement(self):
        safeTiles = [13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,33,34,35,36,37,38,80,81,82,83]
        if pressed[pygame.K_SPACE] and self.walkCounter == 0 and self.attackCounter == 0 and self.attackDelay == 0:
            self.animateCounter = 0
            self.attackCounter = 8
            self.attackDelay = 15
    
        elif pressed[pygame.K_s] and self.walkCounter == 0 and self.attackCounter == 0:
            self.direction = 0
            if map[self.Tile + 10] in safeTiles and self.Tile not in self.frontBorder:
                self.walkCounter = 32
                self.Tile += 10

        elif pressed[pygame.K_d] and self.walkCounter == 0 and self.attackCounter == 0:
            self.direction = 1
            if map[self.Tile + 1] in safeTiles and self.Tile not in self.rightBorder:
                self.walkCounter = 32
                self.Tile += 1

        elif pressed[pygame.K_w] and self.walkCounter == 0 and self.attackCounter == 0:
            self.direction = 2
            if map[self.Tile - 10] in safeTiles and self.Tile not in self.backBorder:
                self.walkCounter = 32
                self.Tile -= 10

        elif pressed[pygame.K_a] and self.walkCounter == 0 and self.attackCounter == 0:
            self.direction = 3
            if map[self.Tile - 1] in safeTiles and self.Tile not in self.leftBorder:
                self.walkCounter = 32
                self.Tile -= 1
    
        #Face different Directions
        elif pressed[pygame.K_DOWN] and self.walkCounter == 0 and self.attackCounter == 0:
            self.direction = 0
        elif pressed[pygame.K_RIGHT] and self.walkCounter == 0 and self.attackCounter == 0:
            self.direction = 1
        elif pressed[pygame.K_UP] and self.walkCounter == 0 and self.attackCounter == 0:
            self.direction = 2
        elif pressed[pygame.K_LEFT] and self.walkCounter == 0 and self.attackCounter == 0:
            self.direction = 3

        if self.walkCounter > 0:
            self.animate = 1
            if self.direction == 0: self.y = self.y + 2
            elif self.direction == 1: self.x = self.x + 2
            elif self.direction == 2: self.y = self.y - 2
            elif self.direction == 3: self.x = self.x - 2

            self.walkCounter = self.walkCounter - 1
            if self.walkCounter == 0:
                self.animate = 0

        if self.attackCounter == 8: #play slash sound.
            slashSound.play()

        if self.attackCounter > 0:
            self.animate = 2
            self.attackCounter = self.attackCounter - 1
            if self.attackCounter == 0:
                self.animate = 0
                self.attackedTile = 100 
        elif self.attackDelay > 0:
            self.attackDelay = self.attackDelay - 1

    def animateObject(self):
        self.animateCounter += .5

        if int(self.animateCounter) == 18:
            self.animateCounter = 0

    def getAttack(self):
        return self.attackedTile

    def getY(self):
        #self.draw()
        return int(self.y / 64)

    def getPos(self):
        return self.x, self.y
        

class Skeleton:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y

        self.alive = 1

        self.animateCounter = 0
        self.animate = 0
        self.direction = direction
        self.attackDelay = 15

        self.walkCounter = 0
        self.attackCounter = 0

        self.damagedTimer = 0

        self.Tile = int(((self.x - 32 + 64) /64) + (((self.y + 64)/ 64) * 10))

    def draw(self):
        if self.direction == 0: #Front

            if self.animate == 0: #front Idle
                if int(self.animateCounter) == 0: screen.blit(SfrontIdle_000,(self.x,self.y))
                elif int(self.animateCounter) == 1: screen.blit(SfrontIdle_001,(self.x,self.y))
                elif int(self.animateCounter) == 2: screen.blit(SfrontIdle_002,(self.x,self.y))
                elif int(self.animateCounter) == 3: screen.blit(SfrontIdle_003,(self.x,self.y))
                elif int(self.animateCounter) == 4: screen.blit(SfrontIdle_004,(self.x,self.y))
                elif int(self.animateCounter) == 5: screen.blit(SfrontIdle_005,(self.x,self.y))
                elif int(self.animateCounter) == 6: screen.blit(SfrontIdle_006,(self.x,self.y))
                elif int(self.animateCounter) == 7: screen.blit(SfrontIdle_007,(self.x,self.y))
                elif int(self.animateCounter) == 8: screen.blit(SfrontIdle_008,(self.x,self.y))
                elif int(self.animateCounter) == 9: screen.blit(SfrontIdle_009,(self.x,self.y))
                elif int(self.animateCounter) == 10: screen.blit(SfrontIdle_010,(self.x,self.y))
                elif int(self.animateCounter) == 11: screen.blit(SfrontIdle_011,(self.x,self.y))

            elif self.animate == 1: #front Walking
                if int(self.animateCounter) == 0: screen.blit(SfrontWalking_000,(self.x,self.y))
                elif int(self.animateCounter) == 1: screen.blit(SfrontWalking_001,(self.x,self.y))
                elif int(self.animateCounter) == 2: screen.blit(SfrontWalking_002,(self.x,self.y))
                elif int(self.animateCounter) == 3: screen.blit(SfrontWalking_003,(self.x,self.y))
                elif int(self.animateCounter) == 4: screen.blit(SfrontWalking_004,(self.x,self.y))
                elif int(self.animateCounter) == 5: screen.blit(SfrontWalking_005,(self.x,self.y))
                elif int(self.animateCounter) == 6: screen.blit(SfrontWalking_006,(self.x,self.y))
                elif int(self.animateCounter) == 7: screen.blit(SfrontWalking_007,(self.x,self.y))
                elif int(self.animateCounter) == 8: screen.blit(SfrontWalking_008,(self.x,self.y))
                elif int(self.animateCounter) == 9: screen.blit(SfrontWalking_009,(self.x,self.y))
                elif int(self.animateCounter) == 10: screen.blit(SfrontWalking_010,(self.x,self.y))
                elif int(self.animateCounter) == 11: screen.blit(SfrontWalking_011,(self.x,self.y))
                elif int(self.animateCounter) == 12: screen.blit(SfrontWalking_012,(self.x,self.y))
                elif int(self.animateCounter) == 13: screen.blit(SfrontWalking_013,(self.x,self.y))
                elif int(self.animateCounter) == 14: screen.blit(SfrontWalking_014,(self.x,self.y))
                elif int(self.animateCounter) == 15: screen.blit(SfrontWalking_015,(self.x,self.y))
                elif int(self.animateCounter) == 16: screen.blit(SfrontWalking_016,(self.x,self.y))
                elif int(self.animateCounter) == 17: screen.blit(SfrontWalking_017,(self.x,self.y))

            elif self.animate == 2:#front Attack
                if int(self.animateCounter) == 0: screen.blit(SfrontSlashing_000,(self.x,self.y))
                elif int(self.animateCounter) == 1: screen.blit(SfrontSlashing_001,(self.x,self.y))
                elif int(self.animateCounter) == 2: screen.blit(SfrontSlashing_002,(self.x,self.y))
                elif int(self.animateCounter) == 3: screen.blit(SfrontSlashing_003,(self.x,self.y))
                elif int(self.animateCounter) == 4: screen.blit(SfrontSlashing_004,(self.x,self.y))
                elif int(self.animateCounter) == 5: screen.blit(SfrontSlashing_005,(self.x,self.y))
                elif int(self.animateCounter) == 6: screen.blit(SfrontSlashing_006,(self.x,self.y))
                elif int(self.animateCounter) == 7: screen.blit(SfrontSlashing_007,(self.x,self.y))
                elif int(self.animateCounter) == 8: screen.blit(SfrontSlashing_008,(self.x,self.y))
    

        elif self.direction == 1: #Right

            if self.animate == 0: #right Idle
                if int(self.animateCounter) == 0: screen.blit(SrightIdle_000,(self.x,self.y))
                elif int(self.animateCounter) == 1: screen.blit(SrightIdle_001,(self.x,self.y))
                elif int(self.animateCounter) == 2: screen.blit(SrightIdle_002,(self.x,self.y))
                elif int(self.animateCounter) == 3: screen.blit(SrightIdle_003,(self.x,self.y))
                elif int(self.animateCounter) == 4: screen.blit(SrightIdle_004,(self.x,self.y))
                elif int(self.animateCounter) == 5: screen.blit(SrightIdle_005,(self.x,self.y))
                elif int(self.animateCounter) == 6: screen.blit(SrightIdle_006,(self.x,self.y))
                elif int(self.animateCounter) == 7: screen.blit(SrightIdle_007,(self.x,self.y))
                elif int(self.animateCounter) == 8: screen.blit(SrightIdle_008,(self.x,self.y))
                elif int(self.animateCounter) == 9: screen.blit(SrightIdle_009,(self.x,self.y))
                elif int(self.animateCounter) == 10: screen.blit(SrightIdle_010,(self.x,self.y))
                elif int(self.animateCounter) == 11: screen.blit(SrightIdle_011,(self.x,self.y))

            elif self.animate == 1: #right Walking
                if int(self.animateCounter) == 0: screen.blit(SrightWalking_000,(self.x,self.y))
                elif int(self.animateCounter) == 1: screen.blit(SrightWalking_001,(self.x,self.y))
                elif int(self.animateCounter) == 2: screen.blit(SrightWalking_002,(self.x,self.y))
                elif int(self.animateCounter) == 3: screen.blit(SrightWalking_003,(self.x,self.y))
                elif int(self.animateCounter) == 4: screen.blit(SrightWalking_004,(self.x,self.y))
                elif int(self.animateCounter) == 5: screen.blit(SrightWalking_005,(self.x,self.y))
                elif int(self.animateCounter) == 6: screen.blit(SrightWalking_006,(self.x,self.y))
                elif int(self.animateCounter) == 7: screen.blit(SrightWalking_007,(self.x,self.y))
                elif int(self.animateCounter) == 8: screen.blit(SrightWalking_008,(self.x,self.y))
                elif int(self.animateCounter) == 9: screen.blit(SrightWalking_009,(self.x,self.y))
                elif int(self.animateCounter) == 10: screen.blit(SrightWalking_010,(self.x,self.y))
                elif int(self.animateCounter) == 11: screen.blit(SrightWalking_011,(self.x,self.y))
                elif int(self.animateCounter) == 12: screen.blit(SrightWalking_012,(self.x,self.y))
                elif int(self.animateCounter) == 13: screen.blit(SrightWalking_013,(self.x,self.y))
                elif int(self.animateCounter) == 14: screen.blit(SrightWalking_014,(self.x,self.y))
                elif int(self.animateCounter) == 15: screen.blit(SrightWalking_015,(self.x,self.y))
                elif int(self.animateCounter) == 16: screen.blit(SrightWalking_016,(self.x,self.y))
                elif int(self.animateCounter) == 17: screen.blit(SrightWalking_017,(self.x,self.y))

            elif self.animate == 2:#right Attack
                if int(self.animateCounter) == 0: screen.blit(SrightSlashing_000,(self.x,self.y))
                elif int(self.animateCounter) == 1: screen.blit(SrightSlashing_001,(self.x,self.y))
                elif int(self.animateCounter) == 2: screen.blit(SrightSlashing_002,(self.x,self.y))
                elif int(self.animateCounter) == 3: screen.blit(SrightSlashing_003,(self.x,self.y))
                elif int(self.animateCounter) == 4: screen.blit(SrightSlashing_004,(self.x,self.y))
                elif int(self.animateCounter) == 5: screen.blit(SrightSlashing_005,(self.x,self.y))
                elif int(self.animateCounter) == 6: screen.blit(SrightSlashing_006,(self.x,self.y))
                elif int(self.animateCounter) == 7: screen.blit(SrightSlashing_007,(self.x,self.y))
                elif int(self.animateCounter) == 8: screen.blit(SrightSlashing_008,(self.x,self.y))

        elif self.direction == 2: #Back

            if self.animate == 0:#back Idle
                if int(self.animateCounter) == 0: screen.blit(SbackIdle_000,(self.x,self.y))
                elif int(self.animateCounter) == 1: screen.blit(SbackIdle_001,(self.x,self.y))
                elif int(self.animateCounter) == 2: screen.blit(SbackIdle_002,(self.x,self.y))
                elif int(self.animateCounter) == 3: screen.blit(SbackIdle_003,(self.x,self.y))
                elif int(self.animateCounter) == 4: screen.blit(SbackIdle_004,(self.x,self.y))
                elif int(self.animateCounter) == 5: screen.blit(SbackIdle_005,(self.x,self.y))
                elif int(self.animateCounter) == 6: screen.blit(SbackIdle_006,(self.x,self.y))
                elif int(self.animateCounter) == 7: screen.blit(SbackIdle_007,(self.x,self.y))
                elif int(self.animateCounter) == 8: screen.blit(SbackIdle_008,(self.x,self.y))
                elif int(self.animateCounter) == 9: screen.blit(SbackIdle_009,(self.x,self.y))
                elif int(self.animateCounter) == 10: screen.blit(SbackIdle_010,(self.x,self.y))
                elif int(self.animateCounter) == 11: screen.blit(SbackIdle_011,(self.x,self.y))


            elif self.animate == 1:#back Walking
                if int(self.animateCounter) == 0: screen.blit(SbackWalking_000,(self.x,self.y))
                elif int(self.animateCounter) == 1: screen.blit(SbackWalking_001,(self.x,self.y))
                elif int(self.animateCounter) == 2: screen.blit(SbackWalking_002,(self.x,self.y))
                elif int(self.animateCounter) == 3: screen.blit(SbackWalking_003,(self.x,self.y))
                elif int(self.animateCounter) == 4: screen.blit(SbackWalking_004,(self.x,self.y))
                elif int(self.animateCounter) == 5: screen.blit(SbackWalking_005,(self.x,self.y))
                elif int(self.animateCounter) == 6: screen.blit(SbackWalking_006,(self.x,self.y))
                elif int(self.animateCounter) == 7: screen.blit(SbackWalking_007,(self.x,self.y))
                elif int(self.animateCounter) == 8: screen.blit(SbackWalking_008,(self.x,self.y))
                elif int(self.animateCounter) == 9: screen.blit(SbackWalking_009,(self.x,self.y))
                elif int(self.animateCounter) == 10: screen.blit(SbackWalking_010,(self.x,self.y))
                elif int(self.animateCounter) == 11: screen.blit(SbackWalking_011,(self.x,self.y))
                elif int(self.animateCounter) == 12: screen.blit(SbackWalking_012,(self.x,self.y))
                elif int(self.animateCounter) == 13: screen.blit(SbackWalking_013,(self.x,self.y))
                elif int(self.animateCounter) == 14: screen.blit(SbackWalking_014,(self.x,self.y))
                elif int(self.animateCounter) == 15: screen.blit(SbackWalking_015,(self.x,self.y))
                elif int(self.animateCounter) == 16: screen.blit(SbackWalking_016,(self.x,self.y))
                elif int(self.animateCounter) == 17: screen.blit(SbackWalking_017,(self.x,self.y))

            elif self.animate == 2:#back Attack
                if int(self.animateCounter) == 0: screen.blit(SbackSlashing_000,(self.x,self.y))
                elif int(self.animateCounter) == 1: screen.blit(SbackSlashing_001,(self.x,self.y))
                elif int(self.animateCounter) == 2: screen.blit(SbackSlashing_002,(self.x,self.y))
                elif int(self.animateCounter) == 3: screen.blit(SbackSlashing_003,(self.x,self.y))
                elif int(self.animateCounter) == 4: screen.blit(SbackSlashing_004,(self.x,self.y))
                elif int(self.animateCounter) == 5: screen.blit(SbackSlashing_005,(self.x,self.y))
                elif int(self.animateCounter) == 6: screen.blit(SbackSlashing_006,(self.x,self.y))
                elif int(self.animateCounter) == 7: screen.blit(SbackSlashing_007,(self.x,self.y))
                elif int(self.animateCounter) == 8: screen.blit(SbackSlashing_008,(self.x,self.y))
    
        elif self.direction == 3: #Left

            if self.animate == 0: #left Idle
                if int(self.animateCounter) == 0: screen.blit(SleftIdle_000,(self.x,self.y))
                elif int(self.animateCounter) == 1: screen.blit(SleftIdle_001,(self.x,self.y))
                elif int(self.animateCounter) == 2: screen.blit(SleftIdle_002,(self.x,self.y))
                elif int(self.animateCounter) == 3: screen.blit(SleftIdle_003,(self.x,self.y))
                elif int(self.animateCounter) == 4: screen.blit(SleftIdle_004,(self.x,self.y))
                elif int(self.animateCounter) == 5: screen.blit(SleftIdle_005,(self.x,self.y))
                elif int(self.animateCounter) == 6: screen.blit(SleftIdle_006,(self.x,self.y))
                elif int(self.animateCounter) == 7: screen.blit(SleftIdle_007,(self.x,self.y))
                elif int(self.animateCounter) == 8: screen.blit(SleftIdle_008,(self.x,self.y))
                elif int(self.animateCounter) == 9: screen.blit(SleftIdle_009,(self.x,self.y))
                elif int(self.animateCounter) == 10: screen.blit(SleftIdle_010,(self.x,self.y))

            elif self.animate == 1: #left Walking
                if int(self.animateCounter) == 0: screen.blit(SleftWalking_000,(self.x,self.y))
                elif int(self.animateCounter) == 1: screen.blit(SleftWalking_001,(self.x,self.y))
                elif int(self.animateCounter) == 2: screen.blit(SleftWalking_002,(self.x,self.y))
                elif int(self.animateCounter) == 3: screen.blit(SleftWalking_003,(self.x,self.y))
                elif int(self.animateCounter) == 4: screen.blit(SleftWalking_004,(self.x,self.y))
                elif int(self.animateCounter) == 5: screen.blit(SleftWalking_005,(self.x,self.y))
                elif int(self.animateCounter) == 6: screen.blit(SleftWalking_006,(self.x,self.y))
                elif int(self.animateCounter) == 7: screen.blit(SleftWalking_007,(self.x,self.y))
                elif int(self.animateCounter) == 8: screen.blit(SleftWalking_008,(self.x,self.y))
                elif int(self.animateCounter) == 9: screen.blit(SleftWalking_009,(self.x,self.y))
                elif int(self.animateCounter) == 10: screen.blit(SleftWalking_010,(self.x,self.y))
                elif int(self.animateCounter) == 11: screen.blit(SleftWalking_011,(self.x,self.y))
                elif int(self.animateCounter) == 12: screen.blit(SleftWalking_012,(self.x,self.y))
                elif int(self.animateCounter) == 13: screen.blit(SleftWalking_013,(self.x,self.y))
                elif int(self.animateCounter) == 14: screen.blit(SleftWalking_014,(self.x,self.y))
                elif int(self.animateCounter) == 15: screen.blit(SleftWalking_015,(self.x,self.y))
                elif int(self.animateCounter) == 16: screen.blit(SleftWalking_016,(self.x,self.y))
                elif int(self.animateCounter) == 17: screen.blit(SleftWalking_017,(self.x,self.y))

            elif self.animate == 2:#left Attack
                if int(self.animateCounter) == 0: screen.blit(SleftSlashing_000,(self.x,self.y))
                elif int(self.animateCounter) == 1: screen.blit(SleftSlashing_001,(self.x,self.y))
                elif int(self.animateCounter) == 2: screen.blit(SleftSlashing_002,(self.x,self.y))
                elif int(self.animateCounter) == 3: screen.blit(SleftSlashing_003,(self.x,self.y))
                elif int(self.animateCounter) == 4: screen.blit(SleftSlashing_004,(self.x,self.y))
                elif int(self.animateCounter) == 5: screen.blit(SleftSlashing_005,(self.x,self.y))
                elif int(self.animateCounter) == 6: screen.blit(SleftSlashing_006,(self.x,self.y))
                elif int(self.animateCounter) == 7: screen.blit(SleftSlashing_007,(self.x,self.y))
                elif int(self.animateCounter) == 8: screen.blit(SleftSlashing_008,(self.x,self.y))
              

    def animateObject(self):
        self.animateCounter += .5
        if int(self.animateCounter) == 12:
            self.animateCounter = -.5

        if self.damagedTimer > 0:
            self.damagedTimer -= 1

    def checkDamage(self,playerAttack):
        if self.Tile == playerAttack:
            if self.damagedTimer == 0: 
                self.alive = 0
                self.y = 320
                self.damagedTimer = 15
                print ("died")

    def checkAlive(self):
        return self.alive
    
    def getY(self):
        #self.draw()
        return int(self.y / 64)

        #print(playerAttack, self.Tile)
##########################################################################################
newTile = 0

map = [ 
7,6,7,6,7,7,6,7,6,7,
11,9,11,9,11,11,9,11,9,11,
15,16,15,16,15,15,16,15,24,25,
21,23,21,21,21,21,21,21,29,39,
26,25,26,25,26,26,26,27,83,45,
41,32,31,32,31,31,31,31,31,44,
43,44,44,44,44,44,44,44,44,44,
]

playMenu = True
while playMenu == True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            #quit()
            sys.exit()

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_ESCAPE]:
       pygame.display.quit()
       pygame.quit() 

    if pressed[pygame.K_SPACE]:
        playMenu = False

    screen.blit(backgroundImage,(0,0))
    pygame.display.update()

##########################################################################################
playGame = True
while playGame == True: #Main Menu

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            #quit()
            sys.exit()

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_ESCAPE]:
       pygame.display.quit()
       pygame.quit()

##########################################################################################

    #Draw Methods

    counter = 0
    counter2 = 0
    for i in map:
        if i == 1:
            screen.blit(tile_1,(counter * 64, counter2 * 64))
        elif i == 2:
            screen.blit(tile_2,(counter * 64, counter2 * 64))
        elif i == 3:
            screen.blit(tile_3,(counter * 64, counter2 * 64))
        elif i == 4:
            screen.blit(tile_4,(counter * 64, counter2 * 64))
        elif i == 5:
            screen.blit(tile_5,(counter * 64, counter2 * 64))
        elif i == 6:
            screen.blit(tile_6,(counter * 64, counter2 * 64))
        elif i == 7:
            screen.blit(tile_7,(counter * 64, counter2 * 64))
        elif i == 8:
            screen.blit(tile_8,(counter * 64, counter2 * 64))
        elif i == 9:
            screen.blit(tile_9,(counter * 64, counter2 * 64))

        elif i == 10:
            screen.blit(tile_10,(counter * 64, counter2 * 64))
        elif i == 11:
            screen.blit(tile_11,(counter * 64, counter2 * 64))
        elif i == 12:
            screen.blit(tile_12,(counter * 64, counter2 * 64))
        elif i == 13:
            screen.blit(tile_13,(counter * 64, counter2 * 64))
        elif i == 14:
            screen.blit(tile_14,(counter * 64, counter2 * 64))
        elif i == 15:
            screen.blit(tile_15,(counter * 64, counter2 * 64))
        elif i == 16:
            screen.blit(tile_16,(counter * 64, counter2 * 64))
        elif i == 17:
            screen.blit(tile_17,(counter * 64, counter2 * 64))
        elif i == 18:
            screen.blit(tile_18,(counter * 64, counter2 * 64))
        elif i == 19:
            screen.blit(tile_19,(counter * 64, counter2 * 64))


        elif i == 20:
            screen.blit(tile_20,(counter * 64, counter2 * 64))
        elif i == 21:
            screen.blit(tile_21,(counter * 64, counter2 * 64))
        elif i == 22:
            screen.blit(tile_22,(counter * 64, counter2 * 64))
        elif i == 23:
            screen.blit(tile_23,(counter * 64, counter2 * 64))
        elif i == 24:
            screen.blit(tile_24,(counter * 64, counter2 * 64))
        elif i == 25:
            screen.blit(tile_25,(counter * 64, counter2 * 64))
        elif i == 26:
            screen.blit(tile_26,(counter * 64, counter2 * 64))
        elif i == 27:
            screen.blit(tile_27,(counter * 64, counter2 * 64))
        elif i == 28:
            screen.blit(tile_28,(counter * 64, counter2 * 64))
        elif i == 29:
            screen.blit(tile_29,(counter * 64, counter2 * 64))
            
        elif i == 30:
            screen.blit(tile_30,(counter * 64, counter2 * 64))
        elif i == 31:
            screen.blit(tile_31,(counter * 64, counter2 * 64))
        elif i == 32:
            screen.blit(tile_32,(counter * 64, counter2 * 64))
        elif i == 33:
            screen.blit(tile_33,(counter * 64, counter2 * 64))
        elif i == 34:
            screen.blit(tile_34,(counter * 64, counter2 * 64))
        elif i == 35:
            screen.blit(tile_35,(counter * 64, counter2 * 64))
        elif i == 36:
            screen.blit(tile_36,(counter * 64, counter2 * 64))
        elif i == 37:
            screen.blit(tile_37,(counter * 64, counter2 * 64))
        elif i == 38:
            screen.blit(tile_38,(counter * 64, counter2 * 64))
        elif i == 39:
            screen.blit(tile_39,(counter * 64, counter2 * 64))
            
        elif i == 40:
            screen.blit(tile_40,(counter * 64, counter2 * 64))
        elif i == 41:
            screen.blit(tile_41,(counter * 64, counter2 * 64))
        elif i == 42:
            screen.blit(tile_42,(counter * 64, counter2 * 64))
        elif i == 43:
            screen.blit(tile_43,(counter * 64, counter2 * 64))
        elif i == 44:
            screen.blit(tile_44,(counter * 64, counter2 * 64))
        elif i == 45:
            screen.blit(tile_45,(counter * 64, counter2 * 64))
        elif i == 46:
            screen.blit(tile_46,(counter * 64, counter2 * 64))
        elif i == 47:
            screen.blit(tile_47,(counter * 64, counter2 * 64))
        elif i == 48:
            screen.blit(tile_48,(counter * 64, counter2 * 64))
        elif i == 49:
            screen.blit(tile_49,(counter * 64, counter2 * 64))

        elif i == 50:
            screen.blit(tile_50,(counter * 64, counter2 * 64))
        elif i == 51:
            screen.blit(tile_51,(counter * 64, counter2 * 64))
        elif i == 52:
            screen.blit(tile_52,(counter * 64, counter2 * 64))
        elif i == 53:
            screen.blit(tile_53,(counter * 64, counter2 * 64))
        elif i == 54:
            screen.blit(tile_54,(counter * 64, counter2 * 64))
        elif i == 55:
            screen.blit(tile_55,(counter * 64, counter2 * 64))
        elif i == 56:
            screen.blit(tile_56,(counter * 64, counter2 * 64))
        elif i == 57:
            screen.blit(tile_57,(counter * 64, counter2 * 64))
        elif i == 58:
            screen.blit(tile_58,(counter * 64, counter2 * 64))
        elif i == 59:
            screen.blit(tile_59,(counter * 64, counter2 * 64))
            
        elif i == 60:
            screen.blit(tile_60,(counter * 64, counter2 * 64))
        elif i == 61:
            screen.blit(tile_61,(counter * 64, counter2 * 64))
        elif i == 62:
            screen.blit(tile_62,(counter * 64, counter2 * 64))
        elif i == 63:
            screen.blit(tile_63,(counter * 64, counter2 * 64))
        elif i == 64:
            screen.blit(tile_64,(counter * 64, counter2 * 64))
        elif i == 65:
            screen.blit(tile_65,(counter * 64, counter2 * 64))
        elif i == 66:
            screen.blit(tile_66,(counter * 64, counter2 * 64))
        elif i == 67:
            screen.blit(tile_67,(counter * 64, counter2 * 64))
        elif i == 68:
            screen.blit(tile_68,(counter * 64, counter2 * 64))
        elif i == 69:
            screen.blit(tile_69,(counter * 64, counter2 * 64))

        elif i == 70:
            screen.blit(tile_70,(counter * 64, counter2 * 64))
        elif i == 71:
            screen.blit(tile_71,(counter * 64, counter2 * 64))
        elif i == 72:
            screen.blit(tile_72,(counter * 64, counter2 * 64))
        elif i == 73:
            screen.blit(tile_73,(counter * 64, counter2 * 64))
        elif i == 74:
            screen.blit(tile_74,(counter * 64, counter2 * 64))
        elif i == 75:
            screen.blit(tile_75,(counter * 64, counter2 * 64))
        elif i == 76:
            screen.blit(tile_76,(counter * 64, counter2 * 64))
        elif i == 77:
            screen.blit(tile_77,(counter * 64, counter2 * 64))
        elif i == 78:
            screen.blit(tile_78,(counter * 64, counter2 * 64))
        elif i == 79:
            screen.blit(tile_79,(counter * 64, counter2 * 64))

        elif i == 80:
            screen.blit(tile_80,(counter * 64, counter2 * 64))
        elif i == 81:
            screen.blit(tile_81,(counter * 64, counter2 * 64))
        elif i == 82:
            screen.blit(tile_82,(counter * 64, counter2 * 64))
        elif i == 83:
            screen.blit(tile_83,(counter * 64, counter2 * 64))
       
        counter += 1
        if counter == 10:
            counter2 += 1
            counter = 0

##########################################################################################

    EnableMapEditor = False
    if EnableMapEditor == True:
        mousexy = pygame.mouse.get_pos()
        mousex = mousexy[0] / 64
        mousey = mousexy[1] / 64
    
        mouseTile = (int(mousex) + (int(mousey)* 10))

        if pressed[pygame.K_RIGHT]:
            if map[mouseTile] < 83:
                map[mouseTile] = map[mouseTile] + 1
                pygame.time.delay(70)

        elif pressed[pygame.K_LEFT]:
            if map[mouseTile] > 0:
                map[mouseTile] = map[mouseTile] - 1
                pygame.time.delay(70)

        if (pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL])  and pressed[pygame.K_s]:
            text_file = open("editor.txt","w")

            txtCounter = 0
            for i in range(7):
                text_file.write( str(map[txtCounter])+ ',' + 
                                 str(map[txtCounter + 1]) + ',' +
                                 str(map[txtCounter + 2]) + ',' +
                                 str(map[txtCounter + 3]) + ',' +
                                 str(map[txtCounter + 4]) + ',' +
                                 str(map[txtCounter + 5]) + ',' +
                                 str(map[txtCounter + 6]) + ',' +
                                 str(map[txtCounter + 7]) + ',' +
                                 str(map[txtCounter + 8]) + ',' +
                                 str(map[txtCounter + 9]) + ',\n')
                txtCounter += 10
            print ("SAVED THE MAP!")
            pygame.time.delay(100)
##########################################################################################

    

##########################################################################################
    

##########################################################################################

   
        
##########################################################################################
    if oneTime == True:
        sk = Skeleton(64 - 32,64 * 2,0)
        s1 = Skeleton((64 * 5) - 32,64 * 3,2)
        P = Player()
        
        #pygame.mixer.music.load('mainMusic.mp3')
        #pygame.mixer.music.play(-1)

        oneTime = False
    
    P.movement()
    P.animateObject()
    P.getAttack()

    #if (sk.checkAlive() == 1):
    #    sk.animateObject()
    sk.checkDamage(P.getAttack())
    #    sk.draw()
        
    #if (s1.checkAlive() == 1):
    #    s1.animateObject()    
    s1.checkDamage(P.getAttack())
    #    s1.draw()

    #P.draw()

    
    #sort by y pos. draw by y pos. //

    #drawZ = [P.draw(),sk.draw(),s1.draw()]
    

    drawZ = [sk.getY() , "sk.draw()",s1.getY() , "s1.draw()", P.getY() , "P.draw()"]

    if drawZ[0] == 0: #NEED TO CHECK IF THE obj IS ALIVE OR NOT!
        eval(drawZ[1])
    if drawZ[2] == 0:
        eval(drawZ[3])
    if drawZ[4] == 0:
        eval(drawZ[5])

    if drawZ[0] == 1:
        eval(drawZ[1])
    if drawZ[2] == 1:
        eval(drawZ[3])
    if drawZ[4] == 1:
        eval(drawZ[5])

    if drawZ[0] == 2:
        eval(drawZ[1])
    if drawZ[2] == 2:
        eval(drawZ[3])
    if drawZ[4] == 2:
        eval(drawZ[5])

    if drawZ[0] == 3:
        eval(drawZ[1])
    if drawZ[2] == 3:
        eval(drawZ[3])
    if drawZ[4] == 3:
        eval(drawZ[5])

    if drawZ[0] == 4:
        eval(drawZ[1])
    if drawZ[2] == 4:
        eval(drawZ[3])
    if drawZ[4] == 4:
        eval(drawZ[5])


##########################################

    playerPos = P.getPos()
    playerX = playerPos[0]
    playerY = playerPos[1]

    if darknessCounter >= 0 and darknessCounter < 5: screen.blit(darkness000,(playerX + 64 - 640,playerY + 64 - 448))
    elif darknessCounter >= 5 and darknessCounter < 10: screen.blit(darkness001,(playerX + 64 - 640,playerY + 64 - 448))
    elif darknessCounter >= 10 and darknessCounter < 15: screen.blit(darkness002,(playerX + 64 - 640,playerY + 64 - 448))
    elif darknessCounter >= 15 and darknessCounter < 20: screen.blit(darkness001,(playerX + 64 - 640,playerY + 64 - 448))

    darknessCounter += 1
    
    if darknessCounter == 20:
        darknessCounter = 0
        
    screen.blit(heartImage,(1280 - 50, 0))
    screen.blit(heartImage,(1280 - 40 - 50, 0))
    screen.blit(heartImage,(1280 - 80 - 50, 0))

    pygame.display.update()

##########################################################################################
    clock.tick(60)
