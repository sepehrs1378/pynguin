from typing import Literal

import random
import math
from dataclasses import dataclass


@dataclass
class Image:
    width: int
    height: int
    channels: int
    pixels: list[list[list[float]]]  # height x width x channels


class ImageProcessor:
    def __init__(self):
        self._intermediate_buffers: list[list[list[list[float]]]] = []
        self._cache: dict[str, list[list[list[float]]]] = {}
        self._current_workspace: list[list[list[float]]] | None = None
        self._image: Image = self._create_random_image()

    def _create_random_image(self, width: int = 4, height: int = 4, channels: int = 3) -> Image:
        pixels = [[[random.random() for _ in range(channels)] for _ in range(width)] for _ in range(height)]
        return Image(width, height, channels, pixels)

    def process_image(
        self,
        operation: Literal["enhance", "denoise", "segment", "transform"],
        quality: Literal["low", "medium", "high", "ultra"] = "medium",
    ) -> Image:
        quality_levels = {"low": 1, "medium": 2, "high": 3, "ultra": 4}
        if quality not in quality_levels:
            raise ValueError(f"Invalid quality level: {quality}")

        downscale_factor = 1.0 / quality_levels[quality]
        kernel_size = quality_levels[quality] * 2 + 1
        iterations = quality_levels[quality]

        working_image = self._image
        if operation == "enhance":
            working_image = self._enhance_image(working_image, kernel_size, iterations)
        elif operation == "denoise":
            working_image = self._denoise_image(working_image, quality_levels[quality])
        elif operation == "segment":
            working_image = self._segment_image(working_image, downscale_factor)
        elif operation == "transform":
            working_image = self._transform_image(working_image, quality_levels[quality])
        else:
            raise ValueError(f"Unknown operation: {operation}")

        if len(self._intermediate_buffers) > 5 or self._image.width * self._image.height > 1000000:
            self._intermediate_buffers.clear()

        return working_image

    def _enhance_image(self, image: Image, kernel_size: int, iterations: int) -> Image:
        kernel = [[random.gauss(0, 1) / (kernel_size**2) for _ in range(kernel_size)] for _ in range(kernel_size)]

        processed_channels = []
        for c in range(image.channels):
            channel_data = [[row[c] for row in col] for col in image.pixels]
            result = [row.copy() for row in channel_data]

            for _ in range(iterations):
                result = self._apply_convolution(result, kernel)
                if iterations > 2:
                    self._intermediate_buffers.append([row.copy() for row in result])

            processed_channels.append(result)

        processed_pixels = [
            [processed_channels[c][i][j] for c in range(image.channels)]
            for i in range(image.height)
            for j in range(image.width)
        ]
        return Image(image.width, image.height, image.channels, processed_pixels)

    def _denoise_image(self, image: Image, strength: int) -> Image:
        denoised = [row.copy() for row in image.pixels]
        for _ in range(strength):
            denoised = self._apply_bilateral_filter(denoised)

        if strength > 2:
            self._current_workspace = [row.copy() for row in denoised]

        return Image(image.width, image.height, image.channels, denoised)

    def _apply_convolution(self, data: list[list[float]], kernel: list[list[float]]) -> list[list[float]]:
        pad = len(kernel) // 2
        padded = self._pad_data(data, pad)
        result = [[0.0 for _ in row] for row in data]

        for i in range(len(data)):
            for j in range(len(data[0])):
                total = 0.0
                for ki in range(len(kernel)):
                    for kj in range(len(kernel[0])):
                        total += padded[i + ki][j + kj] * kernel[ki][kj]
                result[i][j] = total
        return result

    def _pad_data(self, data: list[list[float]], pad: int) -> list[list[float]]:
        height = len(data)
        width = len(data[0]) if height > 0 else 0
        padded = []

        for _ in range(pad):
            padded.append([data[0][0] for _ in range(width + 2 * pad)])

        for row in data:
            new_row = []
            for _ in range(pad):
                new_row.append(row[0])
            new_row.extend(row)
            for _ in range(pad):
                new_row.append(row[-1])
            padded.append(new_row)

        for _ in range(pad):
            padded.append([data[-1][0] for _ in range(width + 2 * pad)])

        return padded

    def _apply_bilateral_filter(self, image: list[list[list[float]]]) -> list[list[list[float]]]:
        result = [row.copy() for row in image]
        diameter = 5
        sigma_color = 0.1
        sigma_space = 5
        pad = diameter // 2

        padded = self._pad_data_rgb(image, pad)

        for i in range(len(image)):
            for j in range(len(image[0])):
                center = padded[i + pad][j + pad]
                total_weight = [0.0, 0.0, 0.0]
                weighted_sum = [0.0, 0.0, 0.0]

                for ki in range(diameter):
                    for kj in range(diameter):
                        pixel = padded[i + ki][j + kj]
                        color_diff = sum((pixel[c] - center[c]) ** 2 for c in range(3))
                        color_weight = math.exp(-color_diff / (2 * sigma_color**2))

                        space_diff = (ki - pad) ** 2 + (kj - pad) ** 2
                        space_weight = math.exp(-space_diff / (2 * sigma_space**2))

                        combined_weight = color_weight * space_weight

                        for c in range(3):
                            weighted_sum[c] += pixel[c] * combined_weight
                            total_weight[c] += combined_weight

                for c in range(3):
                    if total_weight[c] > 0:
                        result[i][j][c] = weighted_sum[c] / total_weight[c]

        return result

    def _pad_data_rgb(self, data: list[list[list[float]]], pad: int) -> list[list[list[float]]]:
        height = len(data)
        width = len(data[0]) if height > 0 else 0
        padded = []

        for _ in range(pad):
            padded.append([data[0][0].copy() for _ in range(width + 2 * pad)])

        for row in data:
            new_row = []
            for _ in range(pad):
                new_row.append(row[0].copy())
            new_row.extend(row)
            for _ in range(pad):
                new_row.append(row[-1].copy())
            padded.append(new_row)

        for _ in range(pad):
            padded.append([data[-1][0].copy() for _ in range(width + 2 * pad)])

        return padded

    def _segment_image(self, image: Image, scale_factor: float) -> Image:
        if scale_factor < 1.0:
            resized = self._resize_image(image.pixels, scale_factor)
        else:
            resized = image.pixels

        mask = [[1 if sum(pixel) / len(pixel) > 0.5 else 0 for pixel in row] for row in resized]

        segmented = [
            [
                [pixel[c] if mask[i][j] == 1 else 0.0 for c in range(image.channels)]
                for i, row in enumerate(image.pixels)
                for j, pixel in enumerate(row)
            ]
        ]

        return Image(image.width, image.height, image.channels, segmented)

    def _transform_image(self, image: Image, complexity: int) -> Image:
        transformed = [row.copy() for row in image.pixels]

        for _ in range(complexity):
            angle = random.uniform(0, 2 * math.pi)
            scale = random.uniform(0.8, 1.2)
            tx = random.uniform(-0.1, 0.1) * image.width
            ty = random.uniform(-0.1, 0.1) * image.height

            cos_angle = math.cos(angle) * scale
            sin_angle = math.sin(angle) * scale

            result = [[[0.0 for _ in range(image.channels)] for _ in range(image.height)] for _ in range(image.width)]

            for i in range(image.height):
                for j in range(image.width):
                    new_j = int(cos_angle * j - sin_angle * i + tx)
                    new_i = int(sin_angle * j + cos_angle * i + ty)

                    if 0 <= new_i < image.height and 0 <= new_j < image.width:
                        for c in range(image.channels):
                            result[i][j][c] = transformed[new_i][new_j][c]

            transformed = result

            if complexity > 2:
                self._intermediate_buffers.append([row.copy() for row in transformed])

        return Image(image.width, image.height, image.channels, transformed)

    def _resize_image(self, image: list[list[list[float]]], factor: float) -> list[list[list[float]]]:
        new_height = int(len(image) * factor)
        new_width = int(len(image[0]) * factor) if len(image) > 0 else 0
        channels = len(image[0][0]) if (len(image) > 0 and len(image[0]) > 0) else 0

        resized = [[[0.0 for _ in range(channels)] for _ in range(new_width)] for _ in range(new_height)]

        for i in range(new_height):
            for j in range(new_width):
                src_i = min(int(i / factor), len(image) - 1)
                src_j = min(int(j / factor), len(image[0]) - 1)
                resized[i][j] = image[src_i][src_j].copy()

        return resized

    def clear_cache(self) -> None:
        self._intermediate_buffers.clear()
        self._cache.clear()
        self._current_workspace = None
