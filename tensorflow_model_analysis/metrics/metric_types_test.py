# Lint as: python3
# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Tests for metric_types."""

from __future__ import absolute_import
from __future__ import division
# Standard __future__ imports
from __future__ import print_function

import tensorflow as tf  # pylint: disable=g-explicit-tensorflow-version-import
from tensorflow_model_analysis.metrics import metric_types


class MetricTypesTest(tf.test.TestCase):

  def testMetricKeyFromProto(self):
    metric_keys = [
        metric_types.MetricKey(name='metric_name'),
        metric_types.MetricKey(
            name='metric_name',
            model_name='model_name',
            output_name='output_name',
            sub_key=metric_types.SubKey(class_id=1),
            is_diff=True),
        metric_types.MetricKey(
            name='metric_name',
            model_name='model_name',
            output_name='output_name',
            sub_key=metric_types.SubKey(top_k=2))
    ]
    for key in metric_keys:
      got_key = metric_types.MetricKey.from_proto(key.to_proto())
      self.assertEqual(key, got_key, '{} != {}'.format(key, got_key))

  def testPlotKeyFromProto(self):
    plot_keys = [
        metric_types.PlotKey(name=''),
        metric_types.PlotKey(
            name='',
            model_name='model_name',
            output_name='output_name',
            sub_key=metric_types.SubKey(class_id=1)),
        metric_types.MetricKey(
            name='',
            model_name='model_name',
            output_name='output_name',
            sub_key=metric_types.SubKey(top_k=2))
    ]
    for key in plot_keys:
      got_key = metric_types.PlotKey.from_proto(key.to_proto())
      self.assertEqual(key, got_key, '{} != {}'.format(key, got_key))


if __name__ == '__main__':
  tf.test.main()
