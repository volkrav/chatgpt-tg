import asyncio
import os
from pathlib import Path


async def get_directory_path(path: str) -> Path:
    '''Return Path'''
    directory_path = Path(await get_base_directory(), path)
    await create_directory(directory_path)
    return directory_path


async def get_base_directory() -> str:
    return str(Path(__file__).absolute().parent.parent)


async def create_directory(directory_path: Path) -> None:
    """
    Check the existence of directory, and create it if it doesn't exist
    """
    if not directory_path.exists():
        directory_path.mkdir(parents=True, exist_ok=True)


async def make_filename_with_path(path: str,
                                  name: str,
                                  extension: str) -> str:
    return f'{path}/{name}.{extension}'


async def ogg_to_mp3(input_path: str, output_path: str) -> None | ValueError:
    # Установка ffmpeg (если необходимо)
    # !apt install ffmpeg

    # Проверяем существование входного ogg файла
    if not os.path.exists(input_path):
        raise ValueError(f"Input file not found: {input_path}")

    # Удаляю предыдущий выходной файл
    _delete_file(output_path)

    # Конвертируем ogg в mp3 с помощью ffmpeg
    cmd = f"ffmpeg -i {input_path} -vn -ar 44100 -ac 2 -ab 192000 -f mp3 {output_path}"
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )

    # Ждем завершения процесса и проверяем наличие ошибок
    _, stderr = await process.communicate()
    if process.returncode != 0:
        error_message = stderr.decode().strip()
        raise ValueError(f"Error during conversion: {error_message}")
    else:
        _delete_file(input_path)


def _delete_file(path):
    if os.path.exists(path):
        os.remove(path)
