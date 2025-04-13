# Borderlands2PS3ProfileEditor
A Python tool to modify Borderlands 2 Profile for PS3

## Instructions
You can choose between two methods
- use a config.ini file
- tui (Text User Interface)

### Using Config File
1. Download Python Files and example config
   1. `payload_lib`, `config.ini` and `update_payload.py`
2. Get save from PS3    
2. Use 'Bruteforce Save Data' to decrypt your PS3 Profile file.
    1. *Before decrypting* - click the verify PFD button. If this fails, it means that one of your config settings is not correct. e.g. for me, I had the wrong console id; I was using the PSID but should have used the IDPS
3. Edit `config.ini`
    1. BarStat values are percentages; the tool currently doesn't prevent invalid values, so don't put in massive values
    2. Golden Keys is limited to 765. (but you can always redo the edit if you run out)    
    4. If you don't want to update a field just comment it out
    5. For now I've limited features to BarStats, BarRank, BarTokens and GoldenKeys as this is what most people are interested in; FOV was a bouns as I was curious if it would work
4. Run the tool

       python3 update_payload.py --config config.ini --payload <path to decrpyted PAYLOAD>
   
   This will create a new `PAYLOAD.new` file in the same location as `PAYLOAD`.
6. Replace `PAYLOAD` with `PAYLOAD.new`
7. Encrypt save using Brutefroce Save Data
8. Copy Save back to PS3

### Using TUI
1. Download or Clone the Project
2. Get save from PS3    
2. Use 'Bruteforce Save Data' to decrypt your PS3 Profile file.
    1. *Before decrypting* - click the verify PFD button. If this fails, it means that one of your config settings is not correct. e.g. for me, I had the wrong console id; I was using the PSID but should have used the IDPS
4. Run the tool

       python3 app.py --payload <path to decrpyted PAYLOAD>
   
5. Edit values and save (use last menu item)
6. This will create a new `PAYLOAD.new` file in the same location as `PAYLOAD`.
7. Replace `PAYLOAD` with `PAYLOAD.new`
8. Encrypt save using Brutefroce Save Data
9. Copy Save back to PS3

## Screenshots
*I used RPCS3 for these imagines* - easier to capture screen with my current setup

### Default FOV

![](/images/fov_70.png)

### Modified FOV

![](/images/fov_90.png)

### Modified Stats - using example `config.ini`.

Note that the perecentages don't match because some values aren't possible in game. e.g.
- 1 token == 1.0 %
- 2 tokens == 1.7 %
- 3 tokens == 2.3 %
  
![](/images/bar_stats.png)

### Tui
![](/images/tui.png)

## Acknowledgements
Unknowingly, the following people helped to create this tool with their publicily available materials
- withmorten
- protobuffers
- swimmesberger
  
I simply stood on the shoulder of giants.
