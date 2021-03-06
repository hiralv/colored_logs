from enum import Enum

class AnimationType(Enum):
    Dots = ['.  ', '.. ', '...']
    Wave = [
        '⸳·⸳․․․․․',
        '․⸳·⸳․․․․',
        '․․⸳·⸳․․․',
        '․․․⸳·⸳․․',
        '․․․․⸳·⸳․',
        '․․․․․⸳·⸳',
        '⸳․․․․․⸳·',
        '·⸳․․․․․⸳'
    ]
    WaveAutoReverse = [
        '⸳·⸳․․․․․',
        '․⸳·⸳․․․․',
        '․․⸳·⸳․․․',
        '․․․⸳·⸳․․',
        '․․․․⸳·⸳․',
        '․․․․․⸳·⸳',
        '․․․․⸳·⸳․',
        '․․․⸳·⸳․․',
        '․․⸳·⸳․․․',
        '․⸳·⸳․․․․'
    ]
    Clock1 = ['⌏', '⌎', '⌌', '⌍']
    Clock2 = ['◴', '◷', '◶', '◵']
    Clock3 = ['◴   ', ' ◷  ', '  ◶ ', '   ◵', '  ◶ ', ' ◷  ']
    Circle = ['◜ ', ' ◝', ' ◞', '◟ ']
    KnightRiderAutoReverse = [
        '▪▫▫▫▫▫▫', '▪▪▫▫▫▫▫', '▪▪▪▫▫▫▫', '▫▪▪▪▫▫▫', '▫▫▪▪▪▫▫', '▫▫▫▪▪▪▫', '▫▫▫▫▪▪▪', '▫▫▫▫▫▪▪',
        '▫▫▫▫▫▫▪', '▫▫▫▫▫▪▪', '▫▫▫▫▪▪▪', '▫▫▫▪▪▪▫', '▫▫▪▪▪▫▫', '▫▪▪▪▫▫▫', '▪▪▪▫▫▫▫', '▪▪▫▫▫▫▫'
    ]
    KnightRider = ['▪▪▫▫▫▫▫', '▪▪▪▫▫▫▫', '▫▪▪▪▫▫▫', '▫▫▪▪▪▫▫', '▫▫▫▪▪▪▫', '▫▫▫▫▪▪▪', '▫▫▫▫▫▪▪']
    Blocks1 = ['▖', '▗', '▝', '▘']
    Blocks2 = ['▚', '▞']
    Blocks3 = ['▟', '▙', '▛', '▜']
    Blocks4 = ['▖', '▗', '▝', '▘', '▚', '▞', '▟', '▙', '▛', '▜', '█']
    BlocksAutoReverse = ['▖', '▗', '▝', '▘', '▚', '▞', '▟', '▙', '▛', '▜', '█', '▜', '▛', '▙', '▟', '▞', '▚', '▘', '▝', '▗']
    Line = ['▓▓▒▒▒▒▒▒', '▓▓▓▒▒▒▒▒', '▒▓▓▓▒▒▒▒', '▒▒▓▓▓▒▒▒', '▒▒▒▓▓▓▒▒', '▒▒▒▒▓▓▓▒', '▒▒▒▒▒▓▓▓', '▒▒▒▒▒▒▓▓', '▓▒▒▒▒▒▒▓']
    LineAutoReverse = [
        '▓▒▒▒▒▒▒▒', '▓▓▒▒▒▒▒▒', '▓▓▓▒▒▒▒▒', '▒▓▓▓▒▒▒▒', '▒▒▓▓▓▒▒▒', '▒▒▒▓▓▓▒▒', '▒▒▒▒▓▓▓▒', '▒▒▒▒▒▓▓▓', '▒▒▒▒▒▒▓▓',
        '▒▒▒▒▒▒▒▓', '▒▒▒▒▒▒▓▓', '▒▒▒▒▒▓▓▓', '▒▒▒▒▓▓▓▒', '▒▒▒▓▓▓▒▒', '▒▒▓▓▓▒▒▒', '▒▓▓▓▒▒▒▒', '▓▓▓▒▒▒▒▒', '▓▓▒▒▒▒▒▒'
    ]
    BlockVerticalFill = ['▁', '▂', '▃', '▅', '▆', '▇']
    BlockVerticalFillAutoReverse = [
        '▁', '▂', '▃', '▅', '▆',
        '▇', '▆', '▅', '▃', '▂'
    ]
    BlockHorizontalFillAutoReverse = [
        '▏', '▎', '▍', '▋', '▊',
        '▉', '▊', '▋', '▍', '▎'
    ]
