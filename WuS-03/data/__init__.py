from typing import Dict
import random as rd

class Urne:
    
    def __init__(self, farben: Dict[str, int]):
        '''
        Constructor, erhält dictionary mit Farben
        und Anzahlen der Kugeln der Farbe
        '''
        self.urne = []
        for farbe, anzahl in farben.items():
            self.urne.extend([farbe for _ in range(anzahl)])
        
            
    def __repr__(self):
        '''
        String Repräsentation der Klasse Urne
        '''
        return 'Die Urne enthält: ' + str(self.urne)
    
    def __len__(self):
        return len(self.urne)
    
    def zieheKugel(self) -> str:
        if len(self.urne) < 1:
            raise ValueError('Urne ist leer!')
        else:
            kugel = rd.choice(self.urne)
            self.urne.remove(kugel)
            return kugel