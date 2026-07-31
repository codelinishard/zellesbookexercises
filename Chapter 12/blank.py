from pokerapp import PokerApp
from textpoker import TextInterface
interface = TextInterface()
app = PokerApp(interface)
app.run()