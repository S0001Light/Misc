import pygame
from pygame.locals import *
from sys import exit

from random import randint

pygame.init()
screen = pygame.display.set_mode((640, 640), RESIZABLE, 32)

while True:
        
        for event in pygame.event.get():
                if event.type == QUIT:
                        exit()
        rand_color = (randint(0,255), randint(0,255), randint(0,255))

        a = 1
        while a in range(-1, 640):
                a += 1
                pos_1 = a
                b = 1
                while b in range(-641, 640):
                        b += 1
                        c = (a, b)
                        screen.set_at(c,rand_color)
                        
        rand_color2 = (int(0), int(0), randint(0,255))

        r = 1
        while r in range(0, 320):
                r += 1
                u = 1
                while u in range(-320, 320):
                        u += 1
                        xU = (r, u)
                        screen.set_at(xU,rand_color2)
        pos_2 = (int(2),int(2))

        screen.set_at(pos_2,rand_color2)

        pos_3 = (int(3),int(3))

        screen.set_at(pos_3,rand_color2)

        pos_4 = (int(4),int(4))

        screen.set_at(pos_4,rand_color2)

        pos_5 = (int(5),int(5))

        screen.set_at(pos_5,rand_color2)

        pos_6 = (int(6),int(6))

        screen.set_at(pos_6,rand_color2)

        pos_7 = (int(7),int(7))

        screen.set_at(pos_7,rand_color2)

        pos_8 = (int(8),int(8))

        screen.set_at(pos_8,rand_color2)

        pos_9 = (int(9),int(9))

        screen.set_at(pos_9,rand_color2)

        pos_10 = (int(10),int(10))

        screen.set_at(pos_10,rand_color2)

        pos_11 = (int(11),int(11))

        screen.set_at(pos_11,rand_color2)

        pos_12 = (int(12),int(12))

        screen.set_at(pos_12,rand_color2)

        pos_13 = (int(13),int(13))

        screen.set_at(pos_13,rand_color2)

        pos_14 = (int(14),int(14))

        screen.set_at(pos_14,rand_color2)

        pos_15 = (int(15),int(15))

        screen.set_at(pos_15,rand_color2)

        pos_16 = (int(16),int(16))

        screen.set_at(pos_16,rand_color2)

        pos_17 = (int(17),int(17))

        screen.set_at(pos_17,rand_color2)

        pos_18 = (int(18),int(18))

        screen.set_at(pos_18,rand_color2)

        pos_19 = (int(19),int(19))

        screen.set_at(pos_19,rand_color2)

        pos_20 = (int(20),int(20))

        screen.set_at(pos_20,rand_color2)

        pos_21 = (int(21),int(21))

        screen.set_at(pos_21,rand_color2)

        pos_22 = (int(22),int(22))

        screen.set_at(pos_22,rand_color2)

        pos_23 = (int(23),int(23))

        screen.set_at(pos_23,rand_color2)

        pos_24 = (int(24),int(24))

        screen.set_at(pos_24,rand_color2)

        pos_25 = (int(25),int(25))

        screen.set_at(pos_25,rand_color2)

        pos_26 = (int(26),int(26))

        screen.set_at(pos_26,rand_color2)

        pos_27 = (int(27),int(27))

        screen.set_at(pos_27,rand_color2)

        pos_28 = (int(28),int(28))

        screen.set_at(pos_28,rand_color2)

        pos_29 = (int(29),int(29))

        screen.set_at(pos_29,rand_color2)

        pos_30 = (int(30),int(30))

        screen.set_at(pos_30,rand_color2)

        pos_31 = (int(31),int(31))

        screen.set_at(pos_31,rand_color2)

        pos_32 = (int(32),int(32))

        screen.set_at(pos_32,rand_color2)

        pos_33 = (int(33),int(33))

        screen.set_at(pos_33,rand_color2)

        pos_34 = (int(34),int(34))

        screen.set_at(pos_34,rand_color2)

        pos_35 = (int(35),int(35))

        screen.set_at(pos_35,rand_color2)

        pos_36 = (int(36),int(36))

        screen.set_at(pos_36,rand_color2)

        pos_37 = (int(37),int(37))

        screen.set_at(pos_37,rand_color2)

        pos_38 = (int(38),int(38))

        screen.set_at(pos_38,rand_color2)

        pos_39 = (int(39),int(39))

        screen.set_at(pos_39,rand_color2)

        pos_40 = (int(40),int(40))

        screen.set_at(pos_40,rand_color2)

        pos_41 = (int(41),int(41))

        screen.set_at(pos_41,rand_color2)

        pos_42 = (int(42),int(42))

        screen.set_at(pos_42,rand_color2)

        pos_43 = (int(43),int(43))

        screen.set_at(pos_43,rand_color2)

        pos_44 = (int(44),int(44))

        screen.set_at(pos_44,rand_color2)

        pos_45 = (int(45),int(45))

        screen.set_at(pos_45,rand_color2)

        pos_46 = (int(46),int(46))

        screen.set_at(pos_46,rand_color2)

        pos_47 = (int(47),int(47))

        screen.set_at(pos_47,rand_color2)

        pos_48 = (int(48),int(48))

        screen.set_at(pos_48,rand_color2)

        pos_49 = (int(49),int(49))

        screen.set_at(pos_49,rand_color2)

        pos_50 = (int(50),int(50))

        screen.set_at(pos_50,rand_color2)

        pos_51 = (int(51),int(51))

        screen.set_at(pos_51,rand_color2)

        pos_52 = (int(52),int(52))

        screen.set_at(pos_52,rand_color2)

        pos_53 = (int(53),int(53))

        screen.set_at(pos_53,rand_color2)

        pos_54 = (int(54),int(54))

        screen.set_at(pos_54,rand_color2)

        pos_55 = (int(55),int(55))

        screen.set_at(pos_55,rand_color2)

        pos_56 = (int(56),int(56))

        screen.set_at(pos_56,rand_color2)

        pos_57 = (int(57),int(57))

        screen.set_at(pos_57,rand_color2)

        pos_58 = (int(58),int(58))

        screen.set_at(pos_58,rand_color2)

        pos_59 = (int(59),int(59))

        screen.set_at(pos_59,rand_color2)

        pos_60 = (int(60),int(60))

        screen.set_at(pos_60,rand_color2)

        pos_61 = (int(61),int(61))

        screen.set_at(pos_61,rand_color2)

        pos_62 = (int(62),int(62))

        screen.set_at(pos_62,rand_color2)

        pos_63 = (int(63),int(63))

        screen.set_at(pos_63,rand_color2)

        pos_64 = (int(64),int(64))

        screen.set_at(pos_64,rand_color2)

        pos_65 = (int(65),int(65))

        screen.set_at(pos_65,rand_color2)

        pos_66 = (int(66),int(66))

        screen.set_at(pos_66,rand_color2)

        pos_67 = (int(67),int(67))

        screen.set_at(pos_67,rand_color2)

        pos_68 = (int(68),int(68))

        screen.set_at(pos_68,rand_color2)

        pos_69 = (int(69),int(69))

        screen.set_at(pos_69,rand_color2)

        pos_70 = (int(70),int(70))

        screen.set_at(pos_70,rand_color2)

        pos_71 = (int(71),int(71))

        screen.set_at(pos_71,rand_color2)

        pos_72 = (int(72),int(72))

        screen.set_at(pos_72,rand_color2)

        pos_73 = (int(73),int(73))

        screen.set_at(pos_73,rand_color2)

        pos_74 = (int(74),int(74))

        screen.set_at(pos_74,rand_color2)

        pos_75 = (int(75),int(75))

        screen.set_at(pos_75,rand_color2)

        pos_76 = (int(76),int(76))

        screen.set_at(pos_76,rand_color2)

        pos_77 = (int(77),int(77))

        screen.set_at(pos_77,rand_color2)

        pos_78 = (int(78),int(78))

        screen.set_at(pos_78,rand_color2)

        pos_79 = (int(79),int(79))

        screen.set_at(pos_79,rand_color2)

        pos_80 = (int(80),int(80))

        screen.set_at(pos_80,rand_color2)

        pos_81 = (int(81),int(81))

        screen.set_at(pos_81,rand_color2)

        pos_82 = (int(82),int(82))

        screen.set_at(pos_82,rand_color2)

        pos_83 = (int(83),int(83))

        screen.set_at(pos_83,rand_color2)

        pos_84 = (int(84),int(84))

        screen.set_at(pos_84,rand_color2)

        pos_85 = (int(85),int(85))

        screen.set_at(pos_85,rand_color2)

        pos_86 = (int(86),int(86))

        screen.set_at(pos_86,rand_color2)

        pos_87 = (int(87),int(87))

        screen.set_at(pos_87,rand_color2)

        pos_88 = (int(88),int(88))

        screen.set_at(pos_88,rand_color2)

        pos_89 = (int(89),int(89))

        screen.set_at(pos_89,rand_color2)

        pos_90 = (int(90),int(90))

        screen.set_at(pos_90,rand_color2)

        pos_91 = (int(91),int(91))

        screen.set_at(pos_91,rand_color2)

        pos_92 = (int(92),int(92))

        screen.set_at(pos_92,rand_color2)

        pos_93 = (int(93),int(93))

        screen.set_at(pos_93,rand_color2)

        pos_94 = (int(94),int(94))

        screen.set_at(pos_94,rand_color2)

        pos_95 = (int(95),int(95))

        screen.set_at(pos_95,rand_color2)

        pos_96 = (int(96),int(96))

        screen.set_at(pos_96,rand_color2)

        pos_97 = (int(97),int(97))

        screen.set_at(pos_97,rand_color2)

        pos_98 = (int(98),int(98))

        screen.set_at(pos_98,rand_color2)

        pos_99 = (int(99),int(99))

        screen.set_at(pos_99,rand_color2)

        pos_100 = (int(100),int(100))

        screen.set_at(pos_100,rand_color2)

        pos_101 = (int(101),int(101))

        screen.set_at(pos_101,rand_color2)

        pos_102 = (int(102),int(102))

        screen.set_at(pos_102,rand_color2)

        pos_103 = (int(103),int(103))

        screen.set_at(pos_103,rand_color2)

        pos_104 = (int(104),int(104))

        screen.set_at(pos_104,rand_color2)

        pos_105 = (int(105),int(105))

        screen.set_at(pos_105,rand_color2)

        pos_106 = (int(106),int(106))

        screen.set_at(pos_106,rand_color2)

        pos_107 = (int(107),int(107))

        screen.set_at(pos_107,rand_color2)

        pos_108 = (int(108),int(108))

        screen.set_at(pos_108,rand_color2)

        pos_109 = (int(109),int(109))

        screen.set_at(pos_109,rand_color2)

        pos_110 = (int(110),int(110))

        screen.set_at(pos_110,rand_color2)

        pos_111 = (int(111),int(111))

        screen.set_at(pos_111,rand_color2)

        pos_112 = (int(112),int(112))

        screen.set_at(pos_112,rand_color2)

        pos_113 = (int(113),int(113))

        screen.set_at(pos_113,rand_color2)

        pos_114 = (int(114),int(114))

        screen.set_at(pos_114,rand_color2)

        pos_115 = (int(115),int(115))

        screen.set_at(pos_115,rand_color2)

        pos_116 = (int(116),int(116))

        screen.set_at(pos_116,rand_color2)

        pos_117 = (int(117),int(117))

        screen.set_at(pos_117,rand_color2)

        pos_118 = (int(118),int(118))

        screen.set_at(pos_118,rand_color2)

        pos_119 = (int(119),int(119))

        screen.set_at(pos_119,rand_color2)

        pos_120 = (int(120),int(120))

        screen.set_at(pos_120,rand_color2)

        pos_121 = (int(121),int(121))

        screen.set_at(pos_121,rand_color2)

        pos_122 = (int(122),int(122))

        screen.set_at(pos_122,rand_color2)

        pos_123 = (int(123),int(123))

        screen.set_at(pos_123,rand_color2)

        pos_124 = (int(124),int(124))

        screen.set_at(pos_124,rand_color2)

        pos_125 = (int(125),int(125))

        screen.set_at(pos_125,rand_color2)

        pos_126 = (int(126),int(126))

        screen.set_at(pos_126,rand_color2)

        pos_127 = (int(127),int(127))

        screen.set_at(pos_127,rand_color2)

        pos_128 = (int(128),int(128))

        screen.set_at(pos_128,rand_color2)

        pos_129 = (int(129),int(129))

        screen.set_at(pos_129,rand_color2)

        pos_130 = (int(130),int(130))

        screen.set_at(pos_130,rand_color2)

        pos_131 = (int(131),int(131))

        screen.set_at(pos_131,rand_color2)

        pos_132 = (int(132),int(132))

        screen.set_at(pos_132,rand_color2)

        pos_133 = (int(133),int(133))

        screen.set_at(pos_133,rand_color2)

        pos_134 = (int(134),int(134))

        screen.set_at(pos_134,rand_color2)

        pos_135 = (int(135),int(135))

        screen.set_at(pos_135,rand_color2)

        pos_136 = (int(136),int(136))

        screen.set_at(pos_136,rand_color2)

        pos_137 = (int(137),int(137))

        screen.set_at(pos_137,rand_color2)

        pos_138 = (int(138),int(138))

        screen.set_at(pos_138,rand_color2)

        pos_139 = (int(139),int(139))

        screen.set_at(pos_139,rand_color2)

        pos_140 = (int(140),int(140))

        screen.set_at(pos_140,rand_color2)

        pos_141 = (int(141),int(141))

        screen.set_at(pos_141,rand_color2)

        pos_142 = (int(142),int(142))

        screen.set_at(pos_142,rand_color2)

        pos_143 = (int(143),int(143))

        screen.set_at(pos_143,rand_color2)

        pos_144 = (int(144),int(144))

        screen.set_at(pos_144,rand_color2)

        pos_145 = (int(145),int(145))

        screen.set_at(pos_145,rand_color2)

        pos_146 = (int(146),int(146))

        screen.set_at(pos_146,rand_color2)

        pos_147 = (int(147),int(147))

        screen.set_at(pos_147,rand_color2)

        pos_148 = (int(148),int(148))

        screen.set_at(pos_148,rand_color2)

        pos_149 = (int(149),int(149))

        screen.set_at(pos_149,rand_color2)

        pos_150 = (int(150),int(150))

        screen.set_at(pos_150,rand_color2)

        pos_151 = (int(151),int(151))

        screen.set_at(pos_151,rand_color2)

        pos_152 = (int(152),int(152))

        screen.set_at(pos_152,rand_color2)

        pos_153 = (int(153),int(153))

        screen.set_at(pos_153,rand_color2)

        pos_154 = (int(154),int(154))

        screen.set_at(pos_154,rand_color2)

        pos_155 = (int(155),int(155))

        screen.set_at(pos_155,rand_color2)

        pos_156 = (int(156),int(156))

        screen.set_at(pos_156,rand_color2)

        pos_157 = (int(157),int(157))

        screen.set_at(pos_157,rand_color2)

        pos_158 = (int(158),int(158))

        screen.set_at(pos_158,rand_color2)

        pos_159 = (int(159),int(159))

        screen.set_at(pos_159,rand_color2)

        pos_160 = (int(160),int(160))

        screen.set_at(pos_160,rand_color2)

        pos_161 = (int(161),int(161))

        screen.set_at(pos_161,rand_color2)

        pos_162 = (int(162),int(162))

        screen.set_at(pos_162,rand_color2)

        pos_163 = (int(163),int(163))

        screen.set_at(pos_163,rand_color2)

        pos_164 = (int(164),int(164))

        screen.set_at(pos_164,rand_color2)

        pos_165 = (int(165),int(165))

        screen.set_at(pos_165,rand_color2)

        pos_166 = (int(166),int(166))

        screen.set_at(pos_166,rand_color2)

        pos_167 = (int(167),int(167))

        screen.set_at(pos_167,rand_color2)

        pos_168 = (int(168),int(168))

        screen.set_at(pos_168,rand_color2)

        pos_169 = (int(169),int(169))

        screen.set_at(pos_169,rand_color2)

        pos_170 = (int(170),int(170))

        screen.set_at(pos_170,rand_color2)

        pos_171 = (int(171),int(171))

        screen.set_at(pos_171,rand_color2)

        pos_172 = (int(172),int(172))

        screen.set_at(pos_172,rand_color2)

        pos_173 = (int(173),int(173))

        screen.set_at(pos_173,rand_color2)

        pos_174 = (int(174),int(174))

        screen.set_at(pos_174,rand_color2)

        pos_175 = (int(175),int(175))

        screen.set_at(pos_175,rand_color2)

        pos_176 = (int(176),int(176))

        screen.set_at(pos_176,rand_color2)

        pos_177 = (int(177),int(177))

        screen.set_at(pos_177,rand_color2)

        pos_178 = (int(178),int(178))

        screen.set_at(pos_178,rand_color2)

        pos_179 = (int(179),int(179))

        screen.set_at(pos_179,rand_color2)

        pos_180 = (int(180),int(180))

        screen.set_at(pos_180,rand_color2)

        pos_181 = (int(181),int(181))

        screen.set_at(pos_181,rand_color2)

        pos_182 = (int(182),int(182))

        screen.set_at(pos_182,rand_color2)

        pos_183 = (int(183),int(183))

        screen.set_at(pos_183,rand_color2)

        pos_184 = (int(184),int(184))

        screen.set_at(pos_184,rand_color2)

        pos_185 = (int(185),int(185))

        screen.set_at(pos_185,rand_color2)

        pos_186 = (int(186),int(186))

        screen.set_at(pos_186,rand_color2)

        pos_187 = (int(187),int(187))

        screen.set_at(pos_187,rand_color2)

        pos_188 = (int(188),int(188))

        screen.set_at(pos_188,rand_color2)

        pos_189 = (int(189),int(189))

        screen.set_at(pos_189,rand_color2)

        pos_190 = (int(190),int(190))

        screen.set_at(pos_190,rand_color2)

        pos_191 = (int(191),int(191))

        screen.set_at(pos_191,rand_color2)

        pos_192 = (int(192),int(192))

        screen.set_at(pos_192,rand_color2)

        pos_193 = (int(193),int(193))

        screen.set_at(pos_193,rand_color2)

        pos_194 = (int(194),int(194))

        screen.set_at(pos_194,rand_color2)

        pos_195 = (int(195),int(195))

        screen.set_at(pos_195,rand_color2)

        pos_196 = (int(196),int(196))

        screen.set_at(pos_196,rand_color2)

        pos_197 = (int(197),int(197))

        screen.set_at(pos_197,rand_color2)

        pos_198 = (int(198),int(198))

        screen.set_at(pos_198,rand_color2)

        pos_199 = (int(199),int(199))

        screen.set_at(pos_199,rand_color2)

        pos_200 = (int(200),int(200))

        screen.set_at(pos_200,rand_color2)

        pos_201 = (int(201),int(201))

        screen.set_at(pos_201,rand_color2)

        pos_202 = (int(202),int(202))

        screen.set_at(pos_202,rand_color2)

        pos_203 = (int(203),int(203))

        screen.set_at(pos_203,rand_color2)

        pos_204 = (int(204),int(204))

        screen.set_at(pos_204,rand_color2)

        pos_205 = (int(205),int(205))

        screen.set_at(pos_205,rand_color2)

        pos_206 = (int(206),int(206))

        screen.set_at(pos_206,rand_color2)

        pos_207 = (int(207),int(207))

        screen.set_at(pos_207,rand_color2)

        pos_208 = (int(208),int(208))

        screen.set_at(pos_208,rand_color2)

        pos_209 = (int(209),int(209))

        screen.set_at(pos_209,rand_color2)

        pos_210 = (int(210),int(210))

        screen.set_at(pos_210,rand_color2)

        pos_211 = (int(211),int(211))

        screen.set_at(pos_211,rand_color2)

        pos_212 = (int(212),int(212))

        screen.set_at(pos_212,rand_color2)

        pos_213 = (int(213),int(213))

        screen.set_at(pos_213,rand_color2)

        pos_214 = (int(214),int(214))

        screen.set_at(pos_214,rand_color2)

        pos_215 = (int(215),int(215))

        screen.set_at(pos_215,rand_color2)

        pos_216 = (int(216),int(216))

        screen.set_at(pos_216,rand_color2)

        pos_217 = (int(217),int(217))

        screen.set_at(pos_217,rand_color2)

        pos_218 = (int(218),int(218))

        screen.set_at(pos_218,rand_color2)

        pos_219 = (int(219),int(219))

        screen.set_at(pos_219,rand_color2)

        pos_220 = (int(220),int(220))

        screen.set_at(pos_220,rand_color2)

        pos_221 = (int(221),int(221))

        screen.set_at(pos_221,rand_color2)

        pos_222 = (int(222),int(222))

        screen.set_at(pos_222,rand_color2)

        pos_223 = (int(223),int(223))

        screen.set_at(pos_223,rand_color2)

        pos_224 = (int(224),int(224))

        screen.set_at(pos_224,rand_color2)

        pos_225 = (int(225),int(225))

        screen.set_at(pos_225,rand_color2)

        pos_226 = (int(226),int(226))

        screen.set_at(pos_226,rand_color2)

        pos_227 = (int(227),int(227))

        screen.set_at(pos_227,rand_color2)

        pos_228 = (int(228),int(228))

        screen.set_at(pos_228,rand_color2)

        pos_229 = (int(229),int(229))

        screen.set_at(pos_229,rand_color2)

        pos_230 = (int(230),int(230))

        screen.set_at(pos_230,rand_color2)

        pos_231 = (int(231),int(231))

        screen.set_at(pos_231,rand_color2)

        pos_232 = (int(232),int(232))

        screen.set_at(pos_232,rand_color2)

        pos_233 = (int(233),int(233))

        screen.set_at(pos_233,rand_color2)

        pos_234 = (int(234),int(234))

        screen.set_at(pos_234,rand_color2)

        pos_235 = (int(235),int(235))

        screen.set_at(pos_235,rand_color2)

        pos_236 = (int(236),int(236))

        screen.set_at(pos_236,rand_color2)

        pos_237 = (int(237),int(237))

        screen.set_at(pos_237,rand_color2)

        pos_238 = (int(238),int(238))

        screen.set_at(pos_238,rand_color2)

        pos_239 = (int(239),int(239))

        screen.set_at(pos_239,rand_color2)

        pos_240 = (int(240),int(240))

        screen.set_at(pos_240,rand_color2)

        pos_241 = (int(241),int(241))

        screen.set_at(pos_241,rand_color2)

        pos_242 = (int(242),int(242))

        screen.set_at(pos_242,rand_color2)

        pos_243 = (int(243),int(243))

        screen.set_at(pos_243,rand_color2)

        pos_244 = (int(244),int(244))

        screen.set_at(pos_244,rand_color2)

        pos_245 = (int(245),int(245))

        screen.set_at(pos_245,rand_color2)

        pos_246 = (int(246),int(246))

        screen.set_at(pos_246,rand_color2)

        pos_247 = (int(247),int(247))

        screen.set_at(pos_247,rand_color2)

        pos_248 = (int(248),int(248))

        screen.set_at(pos_248,rand_color2)

        pos_249 = (int(249),int(249))

        screen.set_at(pos_249,rand_color2)

        pos_250 = (int(250),int(250))

        screen.set_at(pos_250,rand_color2)

        pos_251 = (int(251),int(251))

        screen.set_at(pos_251,rand_color2)

        pos_252 = (int(252),int(252))

        screen.set_at(pos_252,rand_color2)

        pos_253 = (int(253),int(253))

        screen.set_at(pos_253,rand_color2)

        pos_254 = (int(254),int(254))

        screen.set_at(pos_254,rand_color2)

        pos_255 = (int(255),int(255))

        screen.set_at(pos_255,rand_color2)

        pos_256 = (int(256),int(256))

        screen.set_at(pos_256,rand_color2)

        pos_257 = (int(257),int(257))

        screen.set_at(pos_257,rand_color2)

        pos_258 = (int(258),int(258))

        screen.set_at(pos_258,rand_color2)

        pos_259 = (int(259),int(259))

        screen.set_at(pos_259,rand_color2)

        pos_260 = (int(260),int(260))

        screen.set_at(pos_260,rand_color2)

        pos_261 = (int(261),int(261))

        screen.set_at(pos_261,rand_color2)

        pos_262 = (int(262),int(262))

        screen.set_at(pos_262,rand_color2)

        pos_263 = (int(263),int(263))

        screen.set_at(pos_263,rand_color2)

        pos_264 = (int(264),int(264))

        screen.set_at(pos_264,rand_color2)

        pos_265 = (int(265),int(265))

        screen.set_at(pos_265,rand_color2)

        pos_266 = (int(266),int(266))

        screen.set_at(pos_266,rand_color2)

        pos_267 = (int(267),int(267))

        screen.set_at(pos_267,rand_color2)

        pos_268 = (int(268),int(268))

        screen.set_at(pos_268,rand_color2)

        pos_269 = (int(269),int(269))

        screen.set_at(pos_269,rand_color2)

        pos_270 = (int(270),int(270))

        screen.set_at(pos_270,rand_color2)

        pos_271 = (int(271),int(271))

        screen.set_at(pos_271,rand_color2)

        pos_272 = (int(272),int(272))

        screen.set_at(pos_272,rand_color2)

        pos_273 = (int(273),int(273))

        screen.set_at(pos_273,rand_color2)

        pos_274 = (int(274),int(274))

        screen.set_at(pos_274,rand_color2)

        pos_275 = (int(275),int(275))

        screen.set_at(pos_275,rand_color2)

        pos_276 = (int(276),int(276))

        screen.set_at(pos_276,rand_color2)

        pos_277 = (int(277),int(277))

        screen.set_at(pos_277,rand_color2)

        pos_278 = (int(278),int(278))

        screen.set_at(pos_278,rand_color2)

        pos_279 = (int(279),int(279))

        screen.set_at(pos_279,rand_color2)

        pos_280 = (int(280),int(280))

        screen.set_at(pos_280,rand_color2)

        pos_281 = (int(281),int(281))

        screen.set_at(pos_281,rand_color2)

        pos_282 = (int(282),int(282))

        screen.set_at(pos_282,rand_color2)

        pos_283 = (int(283),int(283))

        screen.set_at(pos_283,rand_color2)

        pos_284 = (int(284),int(284))

        screen.set_at(pos_284,rand_color2)

        pos_285 = (int(285),int(285))

        screen.set_at(pos_285,rand_color2)

        pos_286 = (int(286),int(286))

        screen.set_at(pos_286,rand_color2)

        pos_287 = (int(287),int(287))

        screen.set_at(pos_287,rand_color2)

        pos_288 = (int(288),int(288))

        screen.set_at(pos_288,rand_color2)

        pos_289 = (int(289),int(289))

        screen.set_at(pos_289,rand_color2)

        pos_290 = (int(290),int(290))

        screen.set_at(pos_290,rand_color2)

        pos_291 = (int(291),int(291))

        screen.set_at(pos_291,rand_color2)

        pos_292 = (int(292),int(292))

        screen.set_at(pos_292,rand_color2)

        pos_293 = (int(293),int(293))

        screen.set_at(pos_293,rand_color2)

        pos_294 = (int(294),int(294))

        screen.set_at(pos_294,rand_color2)

        pos_295 = (int(295),int(295))

        screen.set_at(pos_295,rand_color2)

        pos_296 = (int(296),int(296))

        screen.set_at(pos_296,rand_color2)

        pos_297 = (int(297),int(297))

        screen.set_at(pos_297,rand_color2)

        pos_298 = (int(298),int(298))

        screen.set_at(pos_298,rand_color2)

        pos_299 = (int(299),int(299))

        screen.set_at(pos_299,rand_color2)

        pos_300 = (int(300),int(300))

        screen.set_at(pos_300,rand_color2)

        pos_301 = (int(301),int(301))

        screen.set_at(pos_301,rand_color2)

        pos_302 = (int(302),int(302))

        screen.set_at(pos_302,rand_color2)

        pos_303 = (int(303),int(303))

        screen.set_at(pos_303,rand_color2)

        pos_304 = (int(304),int(304))

        screen.set_at(pos_304,rand_color2)

        pos_305 = (int(305),int(305))

        screen.set_at(pos_305,rand_color2)

        pos_306 = (int(306),int(306))

        screen.set_at(pos_306,rand_color2)

        pos_307 = (int(307),int(307))

        screen.set_at(pos_307,rand_color2)

        pos_308 = (int(308),int(308))

        screen.set_at(pos_308,rand_color2)

        pos_309 = (int(309),int(309))

        screen.set_at(pos_309,rand_color2)

        pos_310 = (int(310),int(310))

        screen.set_at(pos_310,rand_color2)

        pos_311 = (int(311),int(311))

        screen.set_at(pos_311,rand_color2)

        pos_312 = (int(312),int(312))

        screen.set_at(pos_312,rand_color2)

        pos_313 = (int(313),int(313))

        screen.set_at(pos_313,rand_color2)

        pos_314 = (int(314),int(314))

        screen.set_at(pos_314,rand_color2)

        pos_315 = (int(315),int(315))

        screen.set_at(pos_315,rand_color2)

        pos_316 = (int(316),int(316))

        screen.set_at(pos_316,rand_color2)

        pos_317 = (int(317),int(317))

        screen.set_at(pos_317,rand_color2)

        pos_318 = (int(318),int(318))

        screen.set_at(pos_318,rand_color2)

        pos_319 = (int(319),int(319))

        screen.set_at(pos_319,rand_color2)

        pos_320 = (int(320),int(320))

        screen.set_at(pos_320,rand_color2)

        pos_321 = (int(321),int(321))

        screen.set_at(pos_321,rand_color2)

        pos_322 = (int(322),int(322))

        screen.set_at(pos_322,rand_color2)

        pos_323 = (int(323),int(323))

        screen.set_at(pos_323,rand_color2)

        pos_324 = (int(324),int(324))

        screen.set_at(pos_324,rand_color2)

        pos_325 = (int(325),int(325))

        screen.set_at(pos_325,rand_color2)

        pos_326 = (int(326),int(326))

        screen.set_at(pos_326,rand_color2)

        pos_327 = (int(327),int(327))

        screen.set_at(pos_327,rand_color2)

        pos_328 = (int(328),int(328))

        screen.set_at(pos_328,rand_color2)

        pos_329 = (int(329),int(329))

        screen.set_at(pos_329,rand_color2)

        pos_330 = (int(330),int(330))

        screen.set_at(pos_330,rand_color2)

        pos_331 = (int(331),int(331))

        screen.set_at(pos_331,rand_color2)

        pos_332 = (int(332),int(332))

        screen.set_at(pos_332,rand_color2)

        pos_333 = (int(333),int(333))

        screen.set_at(pos_333,rand_color2)

        pos_334 = (int(334),int(334))

        screen.set_at(pos_334,rand_color2)

        pos_335 = (int(335),int(335))

        screen.set_at(pos_335,rand_color2)

        pos_336 = (int(336),int(336))

        screen.set_at(pos_336,rand_color2)

        pos_337 = (int(337),int(337))

        screen.set_at(pos_337,rand_color2)

        pos_338 = (int(338),int(338))

        screen.set_at(pos_338,rand_color2)

        pos_339 = (int(339),int(339))

        screen.set_at(pos_339,rand_color2)

        pos_340 = (int(340),int(340))

        screen.set_at(pos_340,rand_color2)

        pos_341 = (int(341),int(341))

        screen.set_at(pos_341,rand_color2)

        pos_342 = (int(342),int(342))

        screen.set_at(pos_342,rand_color2)

        pos_343 = (int(343),int(343))

        screen.set_at(pos_343,rand_color2)

        pos_344 = (int(344),int(344))

        screen.set_at(pos_344,rand_color2)

        pos_345 = (int(345),int(345))

        screen.set_at(pos_345,rand_color2)

        pos_346 = (int(346),int(346))

        screen.set_at(pos_346,rand_color2)

        pos_347 = (int(347),int(347))

        screen.set_at(pos_347,rand_color2)

        pos_348 = (int(348),int(348))

        screen.set_at(pos_348,rand_color2)

        pos_349 = (int(349),int(349))

        screen.set_at(pos_349,rand_color2)

        pos_350 = (int(350),int(350))

        screen.set_at(pos_350,rand_color2)

        pos_351 = (int(351),int(351))

        screen.set_at(pos_351,rand_color2)

        pos_352 = (int(352),int(352))

        screen.set_at(pos_352,rand_color2)

        pos_353 = (int(353),int(353))

        screen.set_at(pos_353,rand_color2)

        pos_354 = (int(354),int(354))

        screen.set_at(pos_354,rand_color2)

        pos_355 = (int(355),int(355))

        screen.set_at(pos_355,rand_color2)

        pos_356 = (int(356),int(356))

        screen.set_at(pos_356,rand_color2)

        pos_357 = (int(357),int(357))

        screen.set_at(pos_357,rand_color2)

        pos_358 = (int(358),int(358))

        screen.set_at(pos_358,rand_color2)

        pos_359 = (int(359),int(359))

        screen.set_at(pos_359,rand_color2)

        pos_360 = (int(360),int(360))

        screen.set_at(pos_360,rand_color2)

        pos_361 = (int(361),int(361))

        screen.set_at(pos_361,rand_color2)

        pos_362 = (int(362),int(362))

        screen.set_at(pos_362,rand_color2)

        pos_363 = (int(363),int(363))

        screen.set_at(pos_363,rand_color2)

        pos_364 = (int(364),int(364))

        screen.set_at(pos_364,rand_color2)

        pos_365 = (int(365),int(365))

        screen.set_at(pos_365,rand_color2)

        pos_366 = (int(366),int(366))

        screen.set_at(pos_366,rand_color2)

        pos_367 = (int(367),int(367))

        screen.set_at(pos_367,rand_color2)

        pos_368 = (int(368),int(368))

        screen.set_at(pos_368,rand_color2)

        pos_369 = (int(369),int(369))

        screen.set_at(pos_369,rand_color2)

        pos_370 = (int(370),int(370))

        screen.set_at(pos_370,rand_color2)

        pos_371 = (int(371),int(371))

        screen.set_at(pos_371,rand_color2)

        pos_372 = (int(372),int(372))

        screen.set_at(pos_372,rand_color2)

        pos_373 = (int(373),int(373))

        screen.set_at(pos_373,rand_color2)

        pos_374 = (int(374),int(374))

        screen.set_at(pos_374,rand_color2)

        pos_375 = (int(375),int(375))

        screen.set_at(pos_375,rand_color2)

        pos_376 = (int(376),int(376))

        screen.set_at(pos_376,rand_color2)

        pos_377 = (int(377),int(377))

        screen.set_at(pos_377,rand_color2)

        pos_378 = (int(378),int(378))

        screen.set_at(pos_378,rand_color2)

        pos_379 = (int(379),int(379))

        screen.set_at(pos_379,rand_color2)

        pos_380 = (int(380),int(380))

        screen.set_at(pos_380,rand_color2)

        pos_381 = (int(381),int(381))

        screen.set_at(pos_381,rand_color2)

        pos_382 = (int(382),int(382))

        screen.set_at(pos_382,rand_color2)

        pos_383 = (int(383),int(383))

        screen.set_at(pos_383,rand_color2)

        pos_384 = (int(384),int(384))

        screen.set_at(pos_384,rand_color2)

        pos_385 = (int(385),int(385))

        screen.set_at(pos_385,rand_color2)

        pos_386 = (int(386),int(386))

        screen.set_at(pos_386,rand_color2)

        pos_387 = (int(387),int(387))

        screen.set_at(pos_387,rand_color2)

        pos_388 = (int(388),int(388))

        screen.set_at(pos_388,rand_color2)

        pos_389 = (int(389),int(389))

        screen.set_at(pos_389,rand_color2)

        pos_390 = (int(390),int(390))

        screen.set_at(pos_390,rand_color2)

        pos_391 = (int(391),int(391))

        screen.set_at(pos_391,rand_color2)

        pos_392 = (int(392),int(392))

        screen.set_at(pos_392,rand_color2)

        pos_393 = (int(393),int(393))

        screen.set_at(pos_393,rand_color2)

        pos_394 = (int(394),int(394))

        screen.set_at(pos_394,rand_color2)

        pos_395 = (int(395),int(395))

        screen.set_at(pos_395,rand_color2)

        pos_396 = (int(396),int(396))

        screen.set_at(pos_396,rand_color2)

        pos_397 = (int(397),int(397))

        screen.set_at(pos_397,rand_color2)

        pos_398 = (int(398),int(398))

        screen.set_at(pos_398,rand_color2)

        pos_399 = (int(399),int(399))

        screen.set_at(pos_399,rand_color2)

        pos_400 = (int(400),int(400))

        screen.set_at(pos_400,rand_color2)

        pos_401 = (int(401),int(401))

        screen.set_at(pos_401,rand_color2)

        pos_402 = (int(402),int(402))

        screen.set_at(pos_402,rand_color2)

        pos_403 = (int(403),int(403))

        screen.set_at(pos_403,rand_color2)

        pos_404 = (int(404),int(404))

        screen.set_at(pos_404,rand_color2)

        pos_405 = (int(405),int(405))

        screen.set_at(pos_405,rand_color2)

        pos_406 = (int(406),int(406))

        screen.set_at(pos_406,rand_color2)

        pos_407 = (int(407),int(407))

        screen.set_at(pos_407,rand_color2)

        pos_408 = (int(408),int(408))

        screen.set_at(pos_408,rand_color2)

        pos_409 = (int(409),int(409))

        screen.set_at(pos_409,rand_color2)

        pos_410 = (int(410),int(410))

        screen.set_at(pos_410,rand_color2)

        pos_411 = (int(411),int(411))

        screen.set_at(pos_411,rand_color2)

        pos_412 = (int(412),int(412))

        screen.set_at(pos_412,rand_color2)

        pos_413 = (int(413),int(413))

        screen.set_at(pos_413,rand_color2)

        pos_414 = (int(414),int(414))

        screen.set_at(pos_414,rand_color2)

        pos_415 = (int(415),int(415))

        screen.set_at(pos_415,rand_color2)

        pos_416 = (int(416),int(416))

        screen.set_at(pos_416,rand_color2)

        pos_417 = (int(417),int(417))

        screen.set_at(pos_417,rand_color2)

        pos_418 = (int(418),int(418))

        screen.set_at(pos_418,rand_color2)

        pos_419 = (int(419),int(419))

        screen.set_at(pos_419,rand_color2)

        pos_420 = (int(420),int(420))

        screen.set_at(pos_420,rand_color2)

        pos_421 = (int(421),int(421))

        screen.set_at(pos_421,rand_color2)

        pos_422 = (int(422),int(422))

        screen.set_at(pos_422,rand_color2)

        pos_423 = (int(423),int(423))

        screen.set_at(pos_423,rand_color2)

        pos_424 = (int(424),int(424))

        screen.set_at(pos_424,rand_color2)

        pos_425 = (int(425),int(425))

        screen.set_at(pos_425,rand_color2)

        pos_426 = (int(426),int(426))

        screen.set_at(pos_426,rand_color2)

        pos_427 = (int(427),int(427))

        screen.set_at(pos_427,rand_color2)

        pos_428 = (int(428),int(428))

        screen.set_at(pos_428,rand_color2)

        pos_429 = (int(429),int(429))

        screen.set_at(pos_429,rand_color2)

        pos_430 = (int(430),int(430))

        screen.set_at(pos_430,rand_color2)

        pos_431 = (int(431),int(431))

        screen.set_at(pos_431,rand_color2)

        pos_432 = (int(432),int(432))

        screen.set_at(pos_432,rand_color2)

        pos_433 = (int(433),int(433))

        screen.set_at(pos_433,rand_color2)

        pos_434 = (int(434),int(434))

        screen.set_at(pos_434,rand_color2)

        pos_435 = (int(435),int(435))

        screen.set_at(pos_435,rand_color2)

        pos_436 = (int(436),int(436))

        screen.set_at(pos_436,rand_color2)

        pos_437 = (int(437),int(437))

        screen.set_at(pos_437,rand_color2)

        pos_438 = (int(438),int(438))

        screen.set_at(pos_438,rand_color2)

        pos_439 = (int(439),int(439))

        screen.set_at(pos_439,rand_color2)

        pos_440 = (int(440),int(440))

        screen.set_at(pos_440,rand_color2)

        pos_441 = (int(441),int(441))

        screen.set_at(pos_441,rand_color2)

        pos_442 = (int(442),int(442))

        screen.set_at(pos_442,rand_color2)

        pos_443 = (int(443),int(443))

        screen.set_at(pos_443,rand_color2)

        pos_444 = (int(444),int(444))

        screen.set_at(pos_444,rand_color2)

        pos_445 = (int(445),int(445))

        screen.set_at(pos_445,rand_color2)

        pos_446 = (int(446),int(446))

        screen.set_at(pos_446,rand_color2)

        pos_447 = (int(447),int(447))

        screen.set_at(pos_447,rand_color2)

        pos_448 = (int(448),int(448))

        screen.set_at(pos_448,rand_color2)

        pos_449 = (int(449),int(449))

        screen.set_at(pos_449,rand_color2)

        pos_450 = (int(450),int(450))

        screen.set_at(pos_450,rand_color2)

        pos_451 = (int(451),int(451))

        screen.set_at(pos_451,rand_color2)

        pos_452 = (int(452),int(452))

        screen.set_at(pos_452,rand_color2)

        pos_453 = (int(453),int(453))

        screen.set_at(pos_453,rand_color2)

        pos_454 = (int(454),int(454))

        screen.set_at(pos_454,rand_color2)

        pos_455 = (int(455),int(455))

        screen.set_at(pos_455,rand_color2)

        pos_456 = (int(456),int(456))

        screen.set_at(pos_456,rand_color2)

        pos_457 = (int(457),int(457))

        screen.set_at(pos_457,rand_color2)

        pos_458 = (int(458),int(458))

        screen.set_at(pos_458,rand_color2)

        pos_459 = (int(459),int(459))

        screen.set_at(pos_459,rand_color2)

        pos_460 = (int(460),int(460))

        screen.set_at(pos_460,rand_color2)

        pos_461 = (int(461),int(461))

        screen.set_at(pos_461,rand_color2)

        pos_462 = (int(462),int(462))

        screen.set_at(pos_462,rand_color2)

        pos_463 = (int(463),int(463))

        screen.set_at(pos_463,rand_color2)

        pos_464 = (int(464),int(464))

        screen.set_at(pos_464,rand_color2)

        pos_465 = (int(465),int(465))

        screen.set_at(pos_465,rand_color2)

        pos_466 = (int(466),int(466))

        screen.set_at(pos_466,rand_color2)

        pos_467 = (int(467),int(467))

        screen.set_at(pos_467,rand_color2)

        pos_468 = (int(468),int(468))

        screen.set_at(pos_468,rand_color2)

        pos_469 = (int(469),int(469))

        screen.set_at(pos_469,rand_color2)

        pos_470 = (int(470),int(470))

        screen.set_at(pos_470,rand_color2)

        pos_471 = (int(471),int(471))

        screen.set_at(pos_471,rand_color2)

        pos_472 = (int(472),int(472))

        screen.set_at(pos_472,rand_color2)

        pos_473 = (int(473),int(473))

        screen.set_at(pos_473,rand_color2)

        pos_474 = (int(474),int(474))

        screen.set_at(pos_474,rand_color2)

        pos_475 = (int(475),int(475))

        screen.set_at(pos_475,rand_color2)

        pos_476 = (int(476),int(476))

        screen.set_at(pos_476,rand_color2)

        pos_477 = (int(477),int(477))

        screen.set_at(pos_477,rand_color2)

        pos_478 = (int(478),int(478))

        screen.set_at(pos_478,rand_color2)

        pos_479 = (int(479),int(479))

        screen.set_at(pos_479,rand_color2)

        pos_480 = (int(480),int(480))

        screen.set_at(pos_480,rand_color2)

        pos_481 = (int(481),int(481))

        screen.set_at(pos_481,rand_color2)

        pos_482 = (int(482),int(482))

        screen.set_at(pos_482,rand_color2)

        pos_483 = (int(483),int(483))

        screen.set_at(pos_483,rand_color2)

        pos_484 = (int(484),int(484))

        screen.set_at(pos_484,rand_color2)

        pos_485 = (int(485),int(485))

        screen.set_at(pos_485,rand_color2)

        pos_486 = (int(486),int(486))

        screen.set_at(pos_486,rand_color2)

        pos_487 = (int(487),int(487))

        screen.set_at(pos_487,rand_color2)

        pos_488 = (int(488),int(488))

        screen.set_at(pos_488,rand_color2)

        pos_489 = (int(489),int(489))

        screen.set_at(pos_489,rand_color2)

        pos_490 = (int(490),int(490))

        screen.set_at(pos_490,rand_color2)

        pos_491 = (int(491),int(491))

        screen.set_at(pos_491,rand_color2)

        pos_492 = (int(492),int(492))

        screen.set_at(pos_492,rand_color2)

        pos_493 = (int(493),int(493))

        screen.set_at(pos_493,rand_color2)

        pos_494 = (int(494),int(494))

        screen.set_at(pos_494,rand_color2)

        pos_495 = (int(495),int(495))

        screen.set_at(pos_495,rand_color2)

        pos_496 = (int(496),int(496))

        screen.set_at(pos_496,rand_color2)

        pos_497 = (int(497),int(497))

        screen.set_at(pos_497,rand_color2)

        pos_498 = (int(498),int(498))

        screen.set_at(pos_498,rand_color2)

        pos_499 = (int(499),int(499))

        screen.set_at(pos_499,rand_color2)

        pos_500 = (int(500),int(500))

        screen.set_at(pos_500,rand_color2)

        pos_501 = (int(501),int(501))

        screen.set_at(pos_501,rand_color2)

        pos_502 = (int(502),int(502))

        screen.set_at(pos_502,rand_color2)

        pos_503 = (int(503),int(503))

        screen.set_at(pos_503,rand_color2)

        pos_504 = (int(504),int(504))

        screen.set_at(pos_504,rand_color2)

        pos_505 = (int(505),int(505))

        screen.set_at(pos_505,rand_color2)

        pos_506 = (int(506),int(506))

        screen.set_at(pos_506,rand_color2)

        pos_507 = (int(507),int(507))

        screen.set_at(pos_507,rand_color2)

        pos_508 = (int(508),int(508))

        screen.set_at(pos_508,rand_color2)

        pos_509 = (int(509),int(509))

        screen.set_at(pos_509,rand_color2)

        pos_510 = (int(510),int(510))

        screen.set_at(pos_510,rand_color2)

        pos_511 = (int(511),int(511))

        screen.set_at(pos_511,rand_color2)

        pos_512 = (int(512),int(512))

        screen.set_at(pos_512,rand_color2)

        pos_513 = (int(513),int(513))

        screen.set_at(pos_513,rand_color2)

        pos_514 = (int(514),int(514))

        screen.set_at(pos_514,rand_color2)

        pos_515 = (int(515),int(515))

        screen.set_at(pos_515,rand_color2)

        pos_516 = (int(516),int(516))

        screen.set_at(pos_516,rand_color2)

        pos_517 = (int(517),int(517))

        screen.set_at(pos_517,rand_color2)

        pos_518 = (int(518),int(518))

        screen.set_at(pos_518,rand_color2)

        pos_519 = (int(519),int(519))

        screen.set_at(pos_519,rand_color2)

        pos_520 = (int(520),int(520))

        screen.set_at(pos_520,rand_color2)

        pos_521 = (int(521),int(521))

        screen.set_at(pos_521,rand_color2)

        pos_522 = (int(522),int(522))

        screen.set_at(pos_522,rand_color2)

        pos_523 = (int(523),int(523))

        screen.set_at(pos_523,rand_color2)

        pos_524 = (int(524),int(524))

        screen.set_at(pos_524,rand_color2)

        pos_525 = (int(525),int(525))

        screen.set_at(pos_525,rand_color2)

        pos_526 = (int(526),int(526))

        screen.set_at(pos_526,rand_color2)

        pos_527 = (int(527),int(527))

        screen.set_at(pos_527,rand_color2)

        pos_528 = (int(528),int(528))

        screen.set_at(pos_528,rand_color2)

        pos_529 = (int(529),int(529))

        screen.set_at(pos_529,rand_color2)

        pos_530 = (int(530),int(530))

        screen.set_at(pos_530,rand_color2)

        pos_531 = (int(531),int(531))

        screen.set_at(pos_531,rand_color2)

        pos_532 = (int(532),int(532))

        screen.set_at(pos_532,rand_color2)

        pos_533 = (int(533),int(533))

        screen.set_at(pos_533,rand_color2)

        pos_534 = (int(534),int(534))

        screen.set_at(pos_534,rand_color2)

        pos_535 = (int(535),int(535))

        screen.set_at(pos_535,rand_color2)

        pos_536 = (int(536),int(536))

        screen.set_at(pos_536,rand_color2)

        pos_537 = (int(537),int(537))

        screen.set_at(pos_537,rand_color2)

        pos_538 = (int(538),int(538))

        screen.set_at(pos_538,rand_color2)

        pos_539 = (int(539),int(539))

        screen.set_at(pos_539,rand_color2)

        pos_540 = (int(540),int(540))

        screen.set_at(pos_540,rand_color2)

        pos_541 = (int(541),int(541))

        screen.set_at(pos_541,rand_color2)

        pos_542 = (int(542),int(542))

        screen.set_at(pos_542,rand_color2)

        pos_543 = (int(543),int(543))

        screen.set_at(pos_543,rand_color2)

        pos_544 = (int(544),int(544))

        screen.set_at(pos_544,rand_color2)

        pos_545 = (int(545),int(545))

        screen.set_at(pos_545,rand_color2)

        pos_546 = (int(546),int(546))

        screen.set_at(pos_546,rand_color2)

        pos_547 = (int(547),int(547))

        screen.set_at(pos_547,rand_color2)

        pos_548 = (int(548),int(548))

        screen.set_at(pos_548,rand_color2)

        pos_549 = (int(549),int(549))

        screen.set_at(pos_549,rand_color2)

        pos_550 = (int(550),int(550))

        screen.set_at(pos_550,rand_color2)

        pos_551 = (int(551),int(551))

        screen.set_at(pos_551,rand_color2)

        pos_552 = (int(552),int(552))

        screen.set_at(pos_552,rand_color2)

        pos_553 = (int(553),int(553))

        screen.set_at(pos_553,rand_color2)

        pos_554 = (int(554),int(554))

        screen.set_at(pos_554,rand_color2)

        pos_555 = (int(555),int(555))

        screen.set_at(pos_555,rand_color2)

        pos_556 = (int(556),int(556))

        screen.set_at(pos_556,rand_color2)

        pos_557 = (int(557),int(557))

        screen.set_at(pos_557,rand_color2)

        pos_558 = (int(558),int(558))

        screen.set_at(pos_558,rand_color2)

        pos_559 = (int(559),int(559))

        screen.set_at(pos_559,rand_color2)

        pos_560 = (int(560),int(560))

        screen.set_at(pos_560,rand_color2)

        pos_561 = (int(561),int(561))

        screen.set_at(pos_561,rand_color2)

        pos_562 = (int(562),int(562))

        screen.set_at(pos_562,rand_color2)

        pos_563 = (int(563),int(563))

        screen.set_at(pos_563,rand_color2)

        pos_564 = (int(564),int(564))

        screen.set_at(pos_564,rand_color2)

        pos_565 = (int(565),int(565))

        screen.set_at(pos_565,rand_color2)

        pos_566 = (int(566),int(566))

        screen.set_at(pos_566,rand_color2)

        pos_567 = (int(567),int(567))

        screen.set_at(pos_567,rand_color2)

        pos_568 = (int(568),int(568))

        screen.set_at(pos_568,rand_color2)

        pos_569 = (int(569),int(569))

        screen.set_at(pos_569,rand_color2)

        pos_570 = (int(570),int(570))

        screen.set_at(pos_570,rand_color2)

        pos_571 = (int(571),int(571))

        screen.set_at(pos_571,rand_color2)

        pos_572 = (int(572),int(572))

        screen.set_at(pos_572,rand_color2)

        pos_573 = (int(573),int(573))

        screen.set_at(pos_573,rand_color2)

        pos_574 = (int(574),int(574))

        screen.set_at(pos_574,rand_color2)

        pos_575 = (int(575),int(575))

        screen.set_at(pos_575,rand_color2)

        pos_576 = (int(576),int(576))

        screen.set_at(pos_576,rand_color2)

        pos_577 = (int(577),int(577))

        screen.set_at(pos_577,rand_color2)

        pos_578 = (int(578),int(578))

        screen.set_at(pos_578,rand_color2)

        pos_579 = (int(579),int(579))

        screen.set_at(pos_579,rand_color2)

        pos_580 = (int(580),int(580))

        screen.set_at(pos_580,rand_color2)

        pos_581 = (int(581),int(581))

        screen.set_at(pos_581,rand_color2)

        pos_582 = (int(582),int(582))

        screen.set_at(pos_582,rand_color2)

        pos_583 = (int(583),int(583))

        screen.set_at(pos_583,rand_color2)

        pos_584 = (int(584),int(584))

        screen.set_at(pos_584,rand_color2)

        pos_585 = (int(585),int(585))

        screen.set_at(pos_585,rand_color2)

        pos_586 = (int(586),int(586))

        screen.set_at(pos_586,rand_color2)

        pos_587 = (int(587),int(587))

        screen.set_at(pos_587,rand_color2)

        pos_588 = (int(588),int(588))

        screen.set_at(pos_588,rand_color2)

        pos_589 = (int(589),int(589))

        screen.set_at(pos_589,rand_color2)

        pos_590 = (int(590),int(590))

        screen.set_at(pos_590,rand_color2)

        pos_591 = (int(591),int(591))

        screen.set_at(pos_591,rand_color2)

        pos_592 = (int(592),int(592))

        screen.set_at(pos_592,rand_color2)

        pos_593 = (int(593),int(593))

        screen.set_at(pos_593,rand_color2)

        pos_594 = (int(594),int(594))

        screen.set_at(pos_594,rand_color2)

        pos_595 = (int(595),int(595))

        screen.set_at(pos_595,rand_color2)

        pos_596 = (int(596),int(596))

        screen.set_at(pos_596,rand_color2)

        pos_597 = (int(597),int(597))

        screen.set_at(pos_597,rand_color2)

        pos_598 = (int(598),int(598))

        screen.set_at(pos_598,rand_color2)

        pos_599 = (int(599),int(599))

        screen.set_at(pos_599,rand_color2)

        pos_600 = (int(600),int(600))

        screen.set_at(pos_600,rand_color2)

        pos_601 = (int(601),int(601))

        screen.set_at(pos_601,rand_color2)

        pos_602 = (int(602),int(602))

        screen.set_at(pos_602,rand_color2)

        pos_603 = (int(603),int(603))

        screen.set_at(pos_603,rand_color2)

        pos_604 = (int(604),int(604))

        screen.set_at(pos_604,rand_color2)

        pos_605 = (int(605),int(605))

        screen.set_at(pos_605,rand_color2)

        pos_606 = (int(606),int(606))

        screen.set_at(pos_606,rand_color2)

        pos_607 = (int(607),int(607))

        screen.set_at(pos_607,rand_color2)

        pos_608 = (int(608),int(608))

        screen.set_at(pos_608,rand_color2)

        pos_609 = (int(609),int(609))

        screen.set_at(pos_609,rand_color2)

        pos_610 = (int(610),int(610))

        screen.set_at(pos_610,rand_color2)

        pos_611 = (int(611),int(611))

        screen.set_at(pos_611,rand_color2)

        pos_612 = (int(612),int(612))

        screen.set_at(pos_612,rand_color2)

        pos_613 = (int(613),int(613))

        screen.set_at(pos_613,rand_color2)

        pos_614 = (int(614),int(614))

        screen.set_at(pos_614,rand_color2)

        pos_615 = (int(615),int(615))

        screen.set_at(pos_615,rand_color2)

        pos_616 = (int(616),int(616))

        screen.set_at(pos_616,rand_color2)

        pos_617 = (int(617),int(617))

        screen.set_at(pos_617,rand_color2)

        pos_618 = (int(618),int(618))

        screen.set_at(pos_618,rand_color2)

        pos_619 = (int(619),int(619))

        screen.set_at(pos_619,rand_color2)

        pos_620 = (int(620),int(620))

        screen.set_at(pos_620,rand_color2)

        pos_621 = (int(621),int(621))

        screen.set_at(pos_621,rand_color2)

        pos_622 = (int(622),int(622))

        screen.set_at(pos_622,rand_color2)

        pos_623 = (int(623),int(623))

        screen.set_at(pos_623,rand_color2)

        pos_624 = (int(624),int(624))

        screen.set_at(pos_624,rand_color2)

        pos_625 = (int(625),int(625))

        screen.set_at(pos_625,rand_color2)

        pos_626 = (int(626),int(626))

        screen.set_at(pos_626,rand_color2)

        pos_627 = (int(627),int(627))

        screen.set_at(pos_627,rand_color2)

        pos_628 = (int(628),int(628))

        screen.set_at(pos_628,rand_color2)

        pos_629 = (int(629),int(629))

        screen.set_at(pos_629,rand_color2)

        pos_630 = (int(630),int(630))

        screen.set_at(pos_630,rand_color2)

        pos_631 = (int(631),int(631))

        screen.set_at(pos_631,rand_color2)

        pos_632 = (int(632),int(632))

        screen.set_at(pos_632,rand_color2)

        pos_633 = (int(633),int(633))

        screen.set_at(pos_633,rand_color2)

        pos_634 = (int(634),int(634))

        screen.set_at(pos_634,rand_color2)

        pos_635 = (int(635),int(635))

        screen.set_at(pos_635,rand_color2)

        pos_636 = (int(636),int(636))

        screen.set_at(pos_636,rand_color2)

        pos_637 = (int(637),int(637))

        screen.set_at(pos_637,rand_color2)

        pos_638 = (int(638),int(638))

        screen.set_at(pos_638,rand_color2)

        pos_639 = (int(639),int(639))

        screen.set_at(pos_639,rand_color2)

        pos_640 = (int(640),int(640))

        screen.set_at(pos_640,rand_color2)

        pygame.display.update()
