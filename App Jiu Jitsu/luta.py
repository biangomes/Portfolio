from lutador.main import MeuLutador
from octogono.meuoctogono import MeuOctogono

lutador1 = MeuLutador("Marcus Buchecha", "Nova União", "Jiu Jitsu")
lutador2 = MeuLutador("Tito Ortiz", "Chute Boxe", "Muay Thai")
octogono1 = MeuOctogono(20.0, 10.0, "madeira")

print(f"{lutador1} vs {lutador2} no {octogono1}")