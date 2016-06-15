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

"""Controllers for the moderator page."""

from core.controllers import base
from core.domain import email_manager
from core.domain import summary_services


class ModeratorPage(base.BaseHandler):
    """The moderator page."""

    PAGE_NAME_FOR_CSRF = 'moderator_page'

    @base.require_moderator
    def get(self):
        """Handles GET requests."""
        self.render_template('moderator/moderator.html')


class FeaturedActivitiesHandler(base.BaseHandler):
    """The moderator page handler for featured activities."""

    PAGE_NAME_FOR_CSRF = 'moderator_page'

    @base.require_moderator
    def get(self):
        """Handles GET requests."""
        self.render_json({
            'featured_activity_ids': (
                summary_services.get_featured_activity_ids()),
        })

    @base.require_moderator
    def post(self):
        """Handles POST requests."""
        featured_activity_ids = self.payload.get('featured_activity_ids')
        summary_services.require_activity_ids_to_be_public(
            featured_activity_ids)
        summary_services.update_featured_activity_ids(featured_activity_ids)


class EmailDraftHandler(base.BaseHandler):
    """Provide default email templates for moderator emails."""

    @base.require_moderator
    def get(self, action):
        """Handles GET requests."""
        self.render_json({
            'draft_email_body': (
                email_manager.get_draft_moderator_action_email(action)),
        })
