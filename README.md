# GameCV

GameCV is an innovative project that leverages OpenCV to capture real-time body movements, translating them into game actions—such as ducking, punching, and kicking—for hands-free gameplay. This project demonstrates how computer vision can create immersive and interactive gaming experiences.

## Features

- **Real-time Body Movement Detection:** Uses your webcam to detect specific actions—duck, punch, and kick.
- **Action Mapping:** Maps detected movements to in-game controls, letting you play games with your body.
- **Customizable:** Easily extendable for new gestures and actions.
- **OpenCV Powered:** Robust, real-time processing thanks to OpenCV’s fast video handling and image processing.

## Installation

1. **Clone the Repository**
    ```
    git clone https://github.com/yourusername/GameCV.git
    cd GameCV
    ```

    Make sure your system has a working webcam.

## Usage

1. **Run the Application**
    ```
    python gamecv.py
    ```
2. **Follow On-screen Prompts:**
    - Stand in front of your webcam.
    - Perform duck, punch, or kick movements.
    - Corresponding game actions will be triggered.

## How it Works

GameCV uses OpenCV to process video frames from your webcam. It detects your body posture and specific gestures using computer vision techniques. When a recognized action (duck, punch, kick) is detected, the project simulates keyboard or controller input to control your game character.

| Action | Movement Detected | In-Game Action        |
|--------|-------------------|-----------------------|
| Duck   | Duck posture      | Trigger duck          |
| Punch  | Arm thrust        | Trigger punch         |
| Kick   | Leg movement      | Trigger kick          |

## Contributing

Contributions are welcome! To suggest features or fixes:

- Fork the repo
- Create your feature branch (`git checkout -b feature/AmazingFeature`)
- Commit your changes
- Open a pull request

## Roadmap

- [ ] Add more gesture recognitions
- [ ] Integrate with popular games
- [ ] Improve motion accuracy

## License

This project is licensed under the MIT License.

## Acknowledgements

- [OpenCV](https://opencv.org/) for computer vision tools  
- Community contributors and testers

---

Unleash a new way to play—move, punch, and kick your way through the game world!
