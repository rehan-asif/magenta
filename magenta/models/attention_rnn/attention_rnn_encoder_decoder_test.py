# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Tests for attention_rnn_encoder_decoder."""

# internal imports
import tensorflow as tf

from magenta.models.attention_rnn import attention_rnn_encoder_decoder
from magenta.music import melodies_lib

NOTE_OFF = melodies_lib.MELODY_NOTE_OFF
NO_EVENT = melodies_lib.MELODY_NO_EVENT


class AttentionRnnEncoderDecoderTest(tf.test.TestCase):

  def testDefaultRange(self):
    attention_rnn_encoder_decoder.MIN_NOTE = 48
    attention_rnn_encoder_decoder.MAX_NOTE = 84
    self.assertEqual(attention_rnn_encoder_decoder.TRANSPOSE_TO_KEY, 0)

    melody_encoder_decoder = (
        attention_rnn_encoder_decoder.MelodyEncoderDecoder())
    self.assertEqual(melody_encoder_decoder.input_size, 74)
    self.assertEqual(melody_encoder_decoder.num_classes, 40)

    melody_events = ([48, NO_EVENT, 49, 83, NOTE_OFF] + [NO_EVENT] * 11 +
                     [48, NOTE_OFF] + [NO_EVENT] * 14 +
                     [48, NOTE_OFF, 49, 82])
    melody = melodies_lib.Melody(melody_events)

    melody_indices = [0, 1, 2, 3, 4, 15, 16, 17, 32, 33, 34, 35]
    expected_inputs = [
        [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0,
         1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0,
         1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0,
         1.0, 1.0, 0.0, 1.0, 0.0],
        [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         -1.0, 1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0,
         1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0,
         1.0, 1.0, 0.0, 1.0, 0.0],
        [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0,
         1.0, 1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 1.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0,
         -1.0, -1.0, 1.0, -1.0, -1.0, -1.0, -1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0,
         0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0,
         1.0, 1.0, 1.0, 0.0, 1.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0,
         1.0, -1.0, 1.0, -1.0, -1.0, -1.0, -1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0,
         0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0,
         1.0, 1.0, 1.0, 0.0, 1.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0,
         -1.0, -1.0, -1.0, -1.0, 1.0, -1.0, -1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0,
         0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0,
         1.0, 1.0, 1.0, 0.0, 1.0],
        [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, -1.0, 1.0, 0.0,
         1.0, -1.0, -1.0, -1.0, 1.0, -1.0, -1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0,
         1.0, 1.0, 1.0, 0.0, 1.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, -1.0, 0.0, 0.0,
         -1.0, 1.0, -1.0, -1.0, 1.0, -1.0, -1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0,
         1.0, 1.0, 1.0, 0.0, 1.0],
        [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, -1.0, 1.0, 1.0,
         1.0, -1.0, -1.0, -1.0, -1.0, 1.0, -1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0,
         1.0, 1.0, 1.0, 0.0, 1.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, -1.0, 1.0, 0.0,
         -1.0, 1.0, -1.0, -1.0, -1.0, 1.0, -1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0,
         1.0, 1.0, 1.0, 0.0, 1.0],
        [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0,
         1.0, 1.0, -1.0, -1.0, -1.0, 1.0, -1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0,
         1.0, 1.0, 1.0, 0.0, 1.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0,
         -1.0, -1.0, 1.0, -1.0, -1.0, 1.0, -1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 1.0, 0.0, 0.0, 0.0]
    ]
    expected_labels = [0, 39, 1, 35, 37, 39, 38, 37, 39, 38, 39, 34]
    melodies = [melody, melody]
    full_length_inputs_batch = melody_encoder_decoder.get_inputs_batch(
        melodies, True)

    for i, melody_index in enumerate(melody_indices):
      self.assertListEqual(
          melody_encoder_decoder.events_to_input(melody, melody_index),
          expected_inputs[i])
      self.assertEqual(
          melody_encoder_decoder.events_to_label(melody, melody_index),
          expected_labels[i])
      partial_melody = melodies_lib.Melody(melody_events[:melody_index])
      self.assertEqual(
          melody_encoder_decoder.class_index_to_event(expected_labels[i],
                                                      partial_melody),
          melody_events[melody_index])
      self.assertListEqual(full_length_inputs_batch[0][melody_index],
                           expected_inputs[i])
      self.assertListEqual(full_length_inputs_batch[1][melody_index],
                           expected_inputs[i])
      partial_melody = melodies_lib.Melody(melody_events[:melody_index])
      softmax = [[[0.0] * melody_encoder_decoder.num_classes]]
      softmax[0][0][expected_labels[i]] = 1.0
      melody_encoder_decoder.extend_event_sequences([partial_melody], softmax)
      self.assertEqual(list(partial_melody)[-1], melody_events[melody_index])

    self.assertListEqual(
        [expected_inputs[-1:], expected_inputs[-1:]],
        melody_encoder_decoder.get_inputs_batch(melodies))

  def testCustomRange(self):
    attention_rnn_encoder_decoder.MIN_NOTE = 24
    attention_rnn_encoder_decoder.MAX_NOTE = 36
    self.assertEqual(attention_rnn_encoder_decoder.TRANSPOSE_TO_KEY, 0)

    melody_encoder_decoder = (
        attention_rnn_encoder_decoder.MelodyEncoderDecoder())
    self.assertEqual(melody_encoder_decoder.input_size, 50)
    self.assertEqual(melody_encoder_decoder.num_classes, 16)

    melody_events = ([24, NO_EVENT, 25, 35, NOTE_OFF] + [NO_EVENT] * 11 +
                     [24, NOTE_OFF] + [NO_EVENT] * 14 +
                     [24, NOTE_OFF, 25, 34])
    melody = melodies_lib.Melody(melody_events)

    melody_indices = [0, 1, 2, 3, 4, 15, 16, 17, 32, 33, 34, 35]
    expected_inputs = [
        [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0,
         1.0, 0.0, 0.0, 0.0, 1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 0.0, 1.0,
         1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0,
         1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0],
        [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0,
         0.0, 0.0, 0.0, 0.0, -1.0, 1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 0.0, 1.0,
         1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0,
         1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0],
        [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0,
         1.0, 1.0, 0.0, 0.0, 1.0, 1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 0.0, 0.0,
         1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0,
         1.0, 1.0, 0.0, 0.0, -1.0, -1.0, 1.0, -1.0, -1.0, -1.0, -1.0, 0.0, 1.0,
         1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0,
         0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0,
         1.0, 1.0, 0.0, 0.0, 1.0, -1.0, 1.0, -1.0, -1.0, -1.0, -1.0, 0.0, 1.0,
         1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0,
         0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0,
         0.0, 1.0, 0.0, 0.0, -1.0, -1.0, -1.0, -1.0, 1.0, -1.0, -1.0, 1.0, 1.0,
         1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0,
         0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0],
        [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0,
         1.0, -1.0, 1.0, 0.0, 1.0, -1.0, -1.0, -1.0, 1.0, -1.0, -1.0, 0.0, 1.0,
         1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0,
         0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0,
         1.0, -1.0, 0.0, 0.0, -1.0, 1.0, -1.0, -1.0, 1.0, -1.0, -1.0, 0.0, 1.0,
         1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0,
         0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0],
        [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0,
         1.0, -1.0, 1.0, 1.0, 1.0, -1.0, -1.0, -1.0, -1.0, 1.0, -1.0, 0.0, 1.0,
         1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0,
         0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0,
         1.0, -1.0, 1.0, 0.0, -1.0, 1.0, -1.0, -1.0, -1.0, 1.0, -1.0, 0.0, 1.0,
         1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0,
         0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0],
        [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0,
         1.0, 1.0, 0.0, 1.0, 1.0, 1.0, -1.0, -1.0, -1.0, 1.0, -1.0, 0.0, 0.0,
         1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0,
         0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0,
         1.0, 1.0, 0.0, 0.0, -1.0, -1.0, 1.0, -1.0, -1.0, 1.0, -1.0, 0.0, 0.0,
         1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]
    ]
    expected_labels = [0, 15, 1, 11, 13, 15, 14, 13, 15, 14, 15, 10]
    melodies = [melody, melody]
    full_length_inputs_batch = melody_encoder_decoder.get_inputs_batch(
        melodies, True)

    for i, melody_index in enumerate(melody_indices):
      self.assertListEqual(
          melody_encoder_decoder.events_to_input(melody, melody_index),
          expected_inputs[i])
      self.assertEqual(
          melody_encoder_decoder.events_to_label(melody, melody_index),
          expected_labels[i])
      partial_melody = melodies_lib.Melody(melody_events[:melody_index])
      self.assertEqual(
          melody_encoder_decoder.class_index_to_event(expected_labels[i],
                                                      partial_melody),
          melody_events[melody_index])
      self.assertListEqual(full_length_inputs_batch[0][melody_index],
                           expected_inputs[i])
      self.assertListEqual(full_length_inputs_batch[1][melody_index],
                           expected_inputs[i])
      partial_melody = melodies_lib.Melody(melody_events[:melody_index])
      softmax = [[[0.0] * melody_encoder_decoder.num_classes]]
      softmax[0][0][expected_labels[i]] = 1.0
      melody_encoder_decoder.extend_event_sequences([partial_melody], softmax)
      self.assertEqual(list(partial_melody)[-1], melody_events[melody_index])

    self.assertListEqual(
        [expected_inputs[-1:], expected_inputs[-1:]],
        melody_encoder_decoder.get_inputs_batch(melodies))


if __name__ == '__main__':
  tf.test.main()
