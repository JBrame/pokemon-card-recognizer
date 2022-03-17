from card_recognizer.infra.algo_ops.ops.op import Op
from card_recognizer.infra.api.ffmpeg import FFMPEG


class FFMPEGOp(Op):
    @staticmethod
    def _convert_to_images_wrapper(video_path: str):
        success, image_frames_path = FFMPEG.convert_video_to_frames(
            video_path=video_path
        )
        if not success:
            raise SystemError("FFMPEG conversion failed on " + str(video_path))
        return image_frames_path

    def __init__(self):
        super().__init__(func=self._convert_to_images_wrapper)

    def vis(self) -> None:
        print("Converted " + str(self.input) + ".")

    def vis_input(self) -> None:
        pass

    def save_input(self, out_path: str) -> None:
        pass

    def save_output(self, out_path) -> None:
        pass
