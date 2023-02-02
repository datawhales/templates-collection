from IPython.display import Audio
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

from typing import Tuple, Union


def load_audio(audio_path: str) -> Tuple[np.ndarray, int]:
    """Audio 파일을 불러와서 signal과 sample rate를 반환하는 함수."""
    # signal과 sample rate
    signal, sr = librosa.load(audio_path)
    return signal, sr


def display_audio(signal: np.ndarray, sr: int) -> None:
    """입력된 signal과 sample rate를 이용해 오디오를 재생할 수 있도록 하는 함수."""
    display(Audio(signal, rate=sr))


def plot_waveplot(signal: np.ndarray, sr: int, figsize: Tuple[int, int] = (12, 4)) -> None:
    """입력된 signal과 sample rate를 이용해 waveplot을 그리는 함수."""
    plt.figure(figsize=figsize)

    # plot    
    librosa.display.waveshow(signal, sr=sr)

    plt.title("Waveplot", fontsize=15)
    plt.xlabel("Time", fontsize=12)
    plt.ylabel("Amplitude", fontsize=12)
    plt.tight_layout()
    plt.show()


def plot_fft(signal: np.ndarray, sr: int, figsize: Tuple[int, int] = (12, 4)) -> None:
    """입력된 signal과 sample rate를 이용해 FFT plot을 그리는 함수."""
    plt.figure(figsize=figsize)

    # Discret-Fourier Transform
    fast_fourier_transform = np.fft.fft(signal)

    # magnitude: 각 frequency의 contribution
    magnitude = np.abs(fast_fourier_transform)

    # manginute를 frequency bin에 mapping
    frequency = np.linspace(0, sr, len(magnitude))

    # magnitude와 frequency의 왼쪽 절반 부분만 필요 (대칭이므로)
    left_mag = magnitude[:int(len(magnitude) / 2)]
    left_freq = frequency[:int(len(frequency) / 2)]

    # plot
    plt.plot(left_freq, left_mag)
    plt.title("Discrete-Fourier Transform", fontsize=15)
    plt.xlabel("Frequency", fontsize=12)
    plt.ylabel("Magnitude", fontsize=12)
    plt.tight_layout()
    plt.show()


def plot_spectrogram(signal: np.ndarray, sr: int, n_fft: int = 2048, hop_length: Union[int, None] = None, win_length: Union[int, None] = None, figsize: Tuple[int, int] = (12, 4)) -> None:
    """입력된 signal과 sample rate를 이용해 spectrogram을 그리는 함수.
    
    Args:
        signal (np.ndarray): 음성 신호.
        sr (int): Sample rate.
        n_fft (int): 0으로 padding되는 것을 포함한 fft 되는 sample 수. win_length보다 크거나 같아야 한다.
        hop_length (Union[int, None]): fft마다 이동하는 sample 수 (stride 개념).
        win_length (Union[int, None]): fft 하나에 들어가는 sample 수 (window).
        figsize (Tuple[int, int]): Plot 크기.
    """
    plt.figure(figsize=figsize)

    # Short-Time Fourier Transform
    audio_stft = librosa.stft(signal, n_fft=n_fft, hop_length=hop_length, win_length=win_length)

    # spectrogram 계산
    spectrogram = np.abs(audio_stft)

    # plot
    librosa.display.specshow(spectrogram ,sr=sr, x_axis="time", y_axis="hz", hop_length=hop_length)
    
    plt.colorbar(label="Amplitude")
    plt.title("Spectrogram (Amp)", fontsize=15)
    plt.xlabel("Time", fontsize=12)
    plt.ylabel("Frequency", fontsize=12)
    plt.tight_layout()
    plt.show()


def plot_log_spectrogram(signal: np.ndarray, sr: int, n_fft: int = 2048, hop_length: Union[int, None] = None, win_length: Union[int, None] = None, figsize: Tuple[int, int] = (12, 4)) -> None:
    """입력된 signal과 sample rate를 이용해 log 스케일로 spectrogram을 그리는 함수.

    Args:
        signal (np.ndarray): 음성 신호.
        sr (int): Sample rate.
        n_fft (int): 0으로 padding되는 것을 포함한 fft 되는 sample 수. win_length보다 크거나 같아야 한다.
        hop_length (Union[int, None]): fft마다 이동하는 sample 수 (stride 개념).
        win_length (Union[int, None]): fft 하나에 들어가는 sample 수 (window).
        figsize (Tuple[int, int]): Plot 크기.
    """
    plt.figure(figsize=figsize)

    # Short-Time Fourier Transform
    audio_stft = librosa.stft(signal, n_fft=n_fft, hop_length=hop_length, win_length=win_length)

    # spectrogram 계산
    spectrogram = np.abs(audio_stft)

    # amplitude를 decibel로 변환 (log scale)
    log_spectro = librosa.amplitude_to_db(spectrogram, ref=np.max)

    # plot
    librosa.display.specshow(log_spectro, sr=sr, x_axis="time", y_axis="hz", hop_length=hop_length, cmap="inferno")
    
    plt.colorbar(label="Decibels")
    plt.title("Spectrogram (dB)", fontsize=15)
    plt.xlabel("Time", fontsize=12)
    plt.ylabel("Frequency", fontsize=12)
    plt.tight_layout()
    plt.show()


def plot_mel_spectrogram(signal: np.ndarray, sr: int, n_fft: int = 2048, hop_length: Union[int, None] = None, win_length: Union[int, None] = None, figsize: Tuple[int, int] = (12, 4)) -> None:
    """입력된 signal과 sample rate를 이용해 mel 스케일로 spectrogram을 그리는 함수.

    Args:
        signal (np.ndarray): 음성 신호.
        sr (int): Sample rate.
        n_fft (int): 0으로 padding되는 것을 포함한 fft 되는 sample 수. win_length보다 크거나 같아야 한다.
        hop_length (Union[int, None]): fft마다 이동하는 sample 수 (stride 개념).
        win_length (Union[int, None]): fft 하나에 들어가는 sample 수 (window).
        figsize (Tuple[int, int]): Plot 크기.
    """
    plt.figure(figsize=figsize)

    # mel spectrogram 계산
    mel_signal = librosa.feature.melspectrogram(y=signal, n_fft=n_fft, hop_length=hop_length, win_length=win_length)
    spectrogram = np.abs(mel_signal)

    # power scale을 decibel로 변환
    mel_spectrogram = librosa.power_to_db(spectrogram, ref=np.max)

    # plot
    librosa.display.specshow(mel_spectrogram, sr=sr, x_axis="time", y_axis="mel", hop_length=hop_length, cmap="magma")
    
    plt.colorbar(label="Decibels")
    plt.title("Mel-Spectrogram (dB)", fontsize=15)
    plt.xlabel("Time", fontsize=12)
    plt.ylabel("Frequency", fontsize=12)
    plt.tight_layout()
    plt.show()


def example():
    # librosa 내장 오디오 불러오기
    signal, sr = librosa.load(librosa.util.example("brahms"))

    # Audio 재생
    display(Audio(signal, rate=sr))

    # 오디오 데이터 plot
    plot_waveplot(signal=signal, sr=sr)

    # FFT plot
    plot_fft(signal=signal, sr=sr)

    # spectrogram plot
    plot_spectrogram(signal=signal, sr=sr, n_fft=2048, hop_length=512, win_length=2048)

    # log spectrogram plot
    plot_log_spectrogram(signal=signal, sr=sr, n_fft=2048, hop_length=512, win_length=2048)

    # mel spectrogram plot
    plot_mel_spectrogram(signal=signal, sr=sr, n_fft=2048, hop_length=512, win_length=2048)


if __name__ == "__main__":
    example()
