#!/usr/bin/env python
import ASSR
import sys
import wave
import trim
import merge
import out
merge.merge()
out.out()
ac = ASSR.AudioCorrection('path.wav' , 'tfSessions/2018-10-13-01:40:12-0.8486092/session.ckpt')
ac.process()
ac.saveCorrectedAudio()

