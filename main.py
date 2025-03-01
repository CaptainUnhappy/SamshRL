import train

if __name__ == '__main__':
    '''User Settings'''
    env_config = {
        # Set the path to PyTesseract
        "PYTESSERACT_PATH": r'C:\Program Files\Tesseract-OCR\tesseract.exe',
        "MONITOR": 1,  # Set the monitor to use (1,2,3)
        "DEBUG_MODE": False,  # Renders the AI vision (pretty scuffed)
        "GAME_MODE": "PVP",  # PVP or PVE
        # 1-6 for PVE (look at walkToBoss.py for boss names) | Is ignored for GAME_MODE PVP
        "BOSS": 8,
        # Set to True if the boss has a second phase (only for PVE)
        "BOSS_HAS_SECOND_PHASE": False,
        "PLAYER_HP": 2140,  # Set the player hp (used for hp bar detection)
        # Set the player stamina (used for stamina bar detection)
        "PLAYER_STAMINA": 118,
        # Set the desired fps (used for actions per second) (24 = 2.4 actions per second) #not implemented yet       #My CPU (i9-13900k) can run the training at about 2.4SPS (steps per secons)
        "DESIRED_FPS": 24
    }
    CREATE_NEW_MODEL = True
    # Create a new model or resume training for an existing model

    '''Start Training'''
    print("💍 EldenRL 💍")
    train.train(CREATE_NEW_MODEL, env_config)
