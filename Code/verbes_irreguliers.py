import random

verbes_1 = {
    "casser": ("break", "broke", "broken"),
    "construire": ("build", "built", "built"),
    "attraper": ("catch", "caught", "caught"),
    "faire": ("do", "did", "done"),
    "tomber": ("fall", "fell", "fallen"),
    "obtenir": ("get", "got", "got"),
    "suspendre": ("hang", "hung", "hung"),
    "poser": ("lay", "laid", "laid"),
    "mener": ("lead", "led", "led"),
    "perdre": ("lose", "lost", "lost"),
    "fabriquer": ("make", "made", "made"),
    "tondre": ("mow", "mowed", "mown"),
    "mettre": ("put", "put", "put"),
    "placer": ("set", "set", "set"),
    "secouer": ("shake", "shook", "shaken"),
    "répandre": ("spread", "spread", "spread"),
    "faire tourner": ("spin", "span", "spun"),
    "sauter": ("spring", "sprang", "sprung"),
    "lancer": ("throw", "threw", "thrown"),
    "gagner": ("win", "won", "won"),
    "parier": ("bet", "bet", "bet"),
    "ordonner": ("bid", "bade", "bidden"),
    "pardonner": ("forgive", "forgave", "forgiven"),
    "donner": ("give", "gave", "given"),
    "avoir": ("have", "had", "had"),
    "garder": ("keep", "kept", "kept"),
    "prêter": ("lend", "lent", "lent"),
    "rencontrer": ("meet", "met", "met"),
    "dire": ("say", "said", "said"),
    "envoyer": ("send", "sent", "sent"),
    "montrer": ("show", "showed", "shown"),
    "parler": ("speak", "spoke", "spoken"),
    "épeler": ("spell", "spelt", "spelt"),
    "jurer": ("swear", "swore", "sworn"),
    "prendre": ("take", "took", "taken"),
    "raconter": ("tell", "told", "told"),
    "écrire": ("write", "wrote", "written"),
}

verbes_2 = {
    "battre": ("beat", "beat", "beaten"),
    "mordre": ("bite", "bit", "bitten"),
    "saigner": ("bleed", "bled", "bled"),
    "éclater": ("burst", "burst", "burst"),
    "interdire": ("forbid", "forbade", "forbidden"),
    "frapper": ("hit", "hit", "hit"),
    "blesser": ("hurt", "hurt", "hurt"),
    "tirer": ("shoot", "shot", "shot"),
    "cracher": ("spit", "spat", "spat"),
    "voler": ("steal", "stole", "stolen"),
    "frapper (coup)": ("strike", "struck", "struck"),
    "déchirer": ("tear", "tore", "torn"),
    "subir": ("undergo", "underwent", "undergone"),
    "bouleverser": ("upset", "upset", "upset"),
    "pleurer": ("weep", "wept", "wept"),
    "plier": ("bend", "bent", "bent"),
    "venir": ("come", "came", "come"),
    "conduire": ("drive", "drove", "driven"),
    "voler (air)": ("fly", "flew", "flown"),
    "aller": ("go", "went", "gone"),
    "s'agenouiller": ("kneel", "knelt", "knelt"),
    "pencher": ("lean", "leant", "leant"),
    "partir": ("leave", "left", "left"),
    "faire du cheval": ("ride", "rode", "ridden"),
    "s'élever": ("rise", "rose", "risen"),
    "courir": ("run", "ran", "run"),
    "s'asseoir": ("sit", "sat", "sat"),
    "aller vite": ("speed", "sped", "sped"),
    "marcher à grands pas": ("stride", "strode", "stridden"),
    "se balancer": ("swing", "swung", "swung"),
    "nager": ("swim", "swam", "swum"),
}

input_choice = input("Choisis l'eval (1 ou 2)): ")
if input_choice == "1":
    verbes = verbes_1
else:
    verbes = verbes_2

score = 0
total = len(verbes)
erreurs = []

# ===== UI =====
fenetre = tk.Tk()
fenetre.title("Exemple TextBox")

texte_var = tk.StringVar()

textbox = tk.Entry(fenetre, textvariable=texte_var, width=30)
textbox.pack(pady=10)

def recuperer_texte():
    contenu = texte_var.get()
    print(contenu)

bouton = tk.Button(fenetre, text="Suivant", command=recuperer_texte)
bouton.pack(pady=5)

# ===== logique =====

print("=" * 50)
print("QUIZ VERBES IRRÉGULIERS 🎯 (liste " + input_choice + ")")
print("=" * 50)
print(f"Il y a {total} verbes à conjuguer\n")

for francais, (base, passe, participe) in verbes.items():
    print(f"Verbe français: {francais}")
    
    rep_base = input("  → Base: ").strip().lower()
    rep_passe = input("  → Prétérite: ").strip().lower()
    rep_participe = input("  → Participe passé: ").strip().lower()
    
    bonnes = 0
    if rep_base == base:
        bonnes += 1
    else:
        erreurs.append(f"{francais}: base = {base} (tu as écrit: {rep_base})")
    
    if rep_passe == passe:
        bonnes += 1
    else:
        erreurs.append(f"{francais}: prétérite = {passe} (tu as écrit: {rep_passe})")
    
    if rep_participe == participe:
        bonnes += 1
    else:
        erreurs.append(f"{francais}: participe = {participe} (tu as écrit: {rep_participe})")
    
    score += bonnes
    
    if bonnes == 3:
        print("✅ Parfait!\n")
    elif bonnes >= 1:
        print(f"⚠️  {bonnes}/3 correct(s)\n")
    else:
        print("❌ À revoir\n")

print("\n" + "=" * 50)
print("RÉSULTATS 📊")
print("=" * 50)
print(f"Score: {score}/{total * 3} ({int(score / (total * 3) * 100)}%)")

if erreurs:
    print("\n❌ Erreurs à revoir:")
    for err in erreurs:
        print(f"  • {err}")
else:
    print("\n🔥 PARFAIT!")


fenetre.mainloop()
