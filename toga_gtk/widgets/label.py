from gi.repository import Gtk

from toga.constants import *
from toga.interface import Label as LabelInterface

from .base import WidgetMixin
from ..libs import gtk_alignment


class Label(LabelInterface, WidgetMixin):
    def __init__(self, text, id=None, style=None, alignment=LEFT_ALIGNED):
        super().__init__(id=id, style=style, text=text, alignment=alignment)
        self._create()

    def create(self):
        self._impl = Gtk.Label()
        self._impl.set_line_wrap(False)

        self._impl._interface = self

        self._impl.connect('show', lambda event: self.rehint())

    def _set_alignment(self, value):
        self._impl.set_alignment(*gtk_alignment(self._alignment))

    def _set_text(self, value):
        self._impl.set_text(self._text)

