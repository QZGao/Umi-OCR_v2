# =============================================
# =============== 图片处理连接器 ===============
# =============================================

from .image_provider import copyImage
from .screenshot_controller import ScreenshotController

from PySide2.QtCore import QObject, Slot, Signal


class ImageConnector(QObject):
    # 对所有屏幕截图。传入延时时间。返回截图列表
    @Slot(float, result="QVariant")
    def getScreenshot(self, wait):
        return ScreenshotController.getScreenshot(wait)

    # 对一张图片做裁切。传入原图imgID和裁切参数，返回裁切后的imgID或[Error]
    @Slot(str, int, int, int, int, result=str)
    def getClipImgID(self, imgID, x, y, w, h):
        return ScreenshotController.getClipImgID(imgID, x, y, w, h)

    # 获取当前剪贴板的内容，返回 {"type":"", "": ""}
    @Slot(result="QVariant")
    def getPaste(self):
        return ScreenshotController.getPaste()

    # 将图片写入剪贴板，返回成功与否
    @Slot(str, result=str)
    def copyImage(self, path):
        return copyImage(path)
