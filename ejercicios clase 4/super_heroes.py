puede_volar=str(input("puede volar"))
es_humano=str(input("¿es humano?"))
tiene_mascara=str(input("¿tiene mascara?"))

if puede_volar=="si":
    if es_humano=="si":
        print('ironman')
    else:
        print('captain marvel')
    else:
        if tiene_mascara=="si":
            print('ronan accuser')
        else:
            print('vision')
else:
    if es_humano=="si":
        if tiene_mascara:
            print('spiderman')
        else:
            print('hulk')
        else:
            if tiene_mascara=="si":
                print('black bolt')
            else:
                print('thanos')