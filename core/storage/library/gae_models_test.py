# coding: utf-8
#
# Copyright 2014 The Oppia Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from core.platform import models
from core.tests import test_utils

(library_models,) = models.Registry.import_models([models.NAMES.library])


class ActivityListModelTest(test_utils.GenericTestBase):
    """Tests the ActivityListModel class."""

    def test_featured_activity_list_always_exists(self):
        default_activity_list_model_instance = (
            library_models.ActivityListModel.get('featured'))
        self.assertIsNotNone(default_activity_list_model_instance)
        self.assertEqual(default_activity_list_model_instance.id, 'featured')
        self.assertEqual(default_activity_list_model_instance.activity_ids, [])
