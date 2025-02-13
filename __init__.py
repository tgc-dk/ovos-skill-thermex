# Copyright 2017 Mycroft AI Inc.
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
#
#from shutil import which
#from subprocess import check_output, CalledProcessError

import asyncio
#from ifaddr import get_adapters
from ovos_workshop.decorators import intent_handler
from ovos_workshop.intents import IntentBuilder
from ovos_workshop.skills import OVOSSkill
from ovos_skill_thermex.api import ThermexAPI


class ThermexSkill(OVOSSkill):

    def initialize(self):
        self.api = ThermexAPI("10.0.0.88", "mycroft")

    @intent_handler(IntentBuilder("HoodLightOnIntent").require("hood").require("light").require("on"))
    def handle_hood_lights_on(self, message):
        asyncio.run(self.api.update_light(1))
        self.speak_dialog("hood lights turned on")

        # Needed?
        self.enclosure.activate_mouth_events()
        self.enclosure.mouth_reset()

    @intent_handler(IntentBuilder("HoodLightOffIntent").require("hood").require("light").require("off"))
    def handle_hood_lights_off(self, message):
        asyncio.run(self.api.update_light(0,0))
        self.speak_dialog("hood lights turned off")

        # Needed?
        self.enclosure.activate_mouth_events()
        self.enclosure.mouth_reset()

    @intent_handler(IntentBuilder("HoodOnIntent").require("hood").require("on"))
    def handle_hood_on(self, message):
        asyncio.run(self.api.update_fan(1,2))
        self.speak_dialog("hood turned on")

        # Needed?
        self.enclosure.activate_mouth_events()
        self.enclosure.mouth_reset()

    @intent_handler(IntentBuilder("HoodOffIntent").require("hood").require("off"))
    def handle_hood_off(self, message):
        asyncio.run(self.api.update_fan(0,0))
        self.speak_dialog("hood turned off")

        # Needed?
        self.enclosure.activate_mouth_events()
        self.enclosure.mouth_reset()
