import numpy as np
import matplotlib.pyplot as plt
import time

# パラメータ
initial_temperature = 20.0  # 初期温度 (℃)
target_temperature = 10.0   # 目標温度 (℃)
cooling_rate = 0.5          # 冷却速度の係数 (仮定値)
initial_frequency = 2.4e9   # 初期の動作周波数 (Hz)
frequency_change_rate = 0.1e9  # 周波数の変化率 (Hz/サイクル)

# 干渉パターンを生成
def interference_pattern(x, frequency, amplitude=1.0):
    """逆位相の振動数に基づく干渉パターンを生成する関数"""
    k = 2 * np.pi * frequency
    wave1 = amplitude * np.sin(k * x)
    wave2 = amplitude * np.sin(k * x + np.pi)
    interference = wave1 + wave2
    return interference

# 冷却効果の計算
def cooling_effect(interference, cooling_rate):
    """干渉パターンに基づく冷却効果をモデル化する関数"""
    average_intensity = np.mean(np.abs(interference))
    temperature_change = -cooling_rate * average_intensity
    return temperature_change

# 計算範囲
x = np.linspace(0, 1e-9, 10)  # 時間の短い範囲での計算 (100 ns)
current_temperature = initial_temperature
current_frequency = initial_frequency

# 結果の保存用リスト
temperatures = [current_temperature]
frequencies = [current_frequency]

# シミュレーション
while current_temperature > target_temperature:
    interference = interference_pattern(x, current_frequency)
    temperature_change = cooling_effect(interference, cooling_rate)
    current_temperature += temperature_change
    temperatures.append(current_temperature)
    frequencies.append(current_frequency)
    
    # 動作周波数を更新（動的に変更）
    current_frequency += frequency_change_rate
    
    # 実行中の処理内容を表示
    print(f"動作周波数: {current_frequency/1e9:.2f} GHz, 温度: {current_temperature:.2f} ℃, 温度変化: {temperature_change:.2f} ℃")
    
    # 終了条件チェック
    if temperature_change == 0:
        break  # 冷却効果がない場合はループを終了
    
    # 適切なシミュレーション速度を保つためのスリープ（オプション）
    time.sleep(0.1)  # 0.1秒待機

# 結果の表示
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(frequencies, temperatures, label='温度変化')
plt.xlabel('周波数 (Hz)')
plt.ylabel('温度 (℃)')
plt.legend()
plt.title('周波数と温度の関係')

plt.subplot(1, 2, 2)
plt.bar(['初期温度', '冷却後温度'], [initial_temperature, current_temperature], color=['blue', 'red'])
plt.ylabel('温度 (℃)')
plt.title('温度変化')

plt.tight_layout()
plt.show()

print(f"最終冷却後の温度: {current_temperature:.2f} ℃")