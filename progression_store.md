
# ProgressionStore files

## Overview

ProgressionStore files are used by Speedrunners to store player progress

## File format

```c
// Credit to pop4959

typedef struct Unlock {
    int reward_id;
    byte is_unlocked;
    byte is_new;
};

typedef struct StoryChapter {
    byte level_one;
    byte level_two;
    byte level_three;
    byte level_four;
};

byte unused;
int version;
int current_progression_XP;
byte played_before;
byte played_tutorial_before;
int unlocks_num;
Unlock unlocks[unlocks_num];
int story_difficulty_chapter_one;
StoryChapter chapter_one;
int story_difficulty_chapter_two;
StoryChapter chapter_two;
int story_difficulty_chapter_three;
StoryChapter chapter_three;
int story_difficulty_chapter_four;
StoryChapter chapter_four;
```

## Tools / Resources

- [srprogression - python library for editing ProgressionStore files](https://github.com/commentsr/srprogression)
