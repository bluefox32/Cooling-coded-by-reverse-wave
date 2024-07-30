import Foundation
import UIKit

// パラメータ
var initialTemperature: Double = 20.0
let targetTemperature: Double = 10.0
let coolingRate: Double = 0.5
var currentFrequency: Double = 2.4e9
let frequencyChangeRate: Double = 0.1e9

// 干渉パターンを生成する関数
func interferencePattern(x: Double, frequency: Double, amplitude: Double = 1.0) -> Double {
    let k = 2 * Double.pi * frequency
    let wave1 = amplitude * sin(k * x)
    let wave2 = amplitude * sin(k * x + Double.pi)
    let interference = wave1 + wave2
    return interference
}

// 冷却効果を計算する関数
func coolingEffect(interference: Double, coolingRate: Double) -> Double {
    let averageIntensity = abs(interference)
    let temperatureChange = -coolingRate * averageIntensity
    return temperatureChange
}

// メイン処理
func simulateCooling() {
    var currentTemperature = initialTemperature
    var x: Double = 0.0

    while currentTemperature > targetTemperature {
        let interference = interferencePattern(x: x, frequency: currentFrequency)
        let temperatureChange = coolingEffect(interference: interference, coolingRate: coolingRate)
        currentTemperature += temperatureChange
        
        // 動作周波数の更新
        currentFrequency += frequencyChangeRate
        x += 1e-9 // xの更新
        
        // 結果の表示 (デバッグ用)
        print("動作周波数: \(currentFrequency / 1e9) GHz, 温度: \(currentTemperature) ℃, 温度変化: \(temperatureChange) ℃")
        
        // シミュレーションの一時停止
        Thread.sleep(forTimeInterval: 0.1)
    }

    print("最終冷却後の温度: \(currentTemperature) ℃")
}

// 実行
simulateCooling()