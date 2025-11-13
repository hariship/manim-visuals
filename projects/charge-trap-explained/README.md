# Charge Trap Explained

An educational animation series explaining charge traps in SSDs and the fundamentals of insulators, conductors, and quantum-level data storage.

## Concepts Covered

1. **Insulators vs Conductors** - Basic material properties
2. **Electron Behavior** - How electrons move (or don't) in different materials
3. **SSD Cell Structure** - Floating gate transistor architecture
4. **Charge Trap Mechanism** - How data is stored and why it degrades
5. **Quantum Tunneling** - The physics behind charge injection and retention

## Scenes

### intro.py

- `ChargeTrapIntro` - Title and introduction
- `InsulatorBasics` - Explain insulators vs conductors
- `ElectronMovement` - Visualize electron behavior
- `SSDStructure` - Show SSD cell architecture
- `ChargeTrapMechanism` - Explain charge trapping

## Usage

```bash
# Start live development
python serve.py charge-trap-explained intro ChargeTrapIntro
python tools/watch.py projects/charge-trap-explained/intro.py ChargeTrapIntro

# Render single scene
manim -pql projects/charge-trap-explained/intro.py InsulatorBasics
```

## Technical Details

- **Floating Gate**: Isolated conductor surrounded by insulator
- **Oxide Layer**: Insulator that traps charges
- **Quantum Tunneling**: Electrons can "tunnel" through thin insulators
- **Charge Retention**: How long trapped charges stay (data persistence)
- **Charge Trap Flash (CTF)**: Modern alternative to floating gate

## References

- SSD architecture and NAND flash technology
- Quantum mechanics of tunneling
- Material science: insulators and semiconductors
