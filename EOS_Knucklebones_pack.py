import os

from dev_utils import build
from utils import global_path

global_path.set_proj_abs_path(os.path.abspath(__file__))

build.build(
    withconsole=False,
    path=os.path.abspath("EOS_Knucklebones.py"),
    filedict=["assets"],
    companyname="shißdo",
    product_version="0.0.1",
    icon=global_path.get_proj_abs_path("assets/icon.png"),
)
