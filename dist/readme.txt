Jp bot alpha version >>> 1.0.1

F.A.Q. 

- Cos'è?
	
	Jp bot è un software in grado di inserire automaticamente nel carrello del proprio account cardtrader tutte le inserzioni di una determinata espansione (attualmente solo MTG) che rispettano le seguenti caratteristiche:
	
	1. L'inserzione da inserire nel carrello è NM, IT e ha accesso alla modalità di acquisto CT Zero.
	2. L'inserzione è la più economica in lista.
	3. L'inserzione più economica in lista ha un prezzo minore rispetto alla successiva di almeno x (dove x è un valore piatto, come 2€, oppure una percentuale)


- Perché il software, in alcuni casi, non inserisce nel carrello le effettive inserzioni più economiche oppure inserisce inserzioni non corrette?
	
	Jp bot basa la sua analisi sui dati restituiti dalle API di Cardtrader, questi dati sono però cached e potrebbero non corrispondere precisamente ai valori "reali" visualizzabili sul sito.

- Come funziona?
	
	Per avviare il sw, basta seguire questi passaggi:

	1. Doppio click sul file "jp_bot_alpha_ver.exe".
	2. Nella schermata di login, inserire il proprio token di autenticazione fornito da Cardtrader (se non sai dove trovarlo, segui le istruzioni presenti nella schermata 	di login).
	4. Fare click sul pulsante "Login".
	5. <opzionale> Spuntare la checkbox in modo tale che il sw si ricordi l'auth token per gli accessi futuri.
	6. Nella schermata di home è possibile scegliere il criterio con cui il sw paragona il prezzo della prima inserzione più economica con la seconda.
	7. All'interno dell'input inserire la differenza massima di prezzo, in base a quanto riportato sopra il valore inserito sarà una percentuale o un valore fisso.
	8. Inserire il prezzo massimo (in euro) che il carrello può contenere, se si supera tale soglia il sw smette di lavorare.
	9. All'interno dell'ultimo campo di input, inserire il nome della espansione (MTG) su cui il sw dovrà lavorare, durante l'inserimento dovrebbe anche aprirsi un menù a tendina con tutti i possibili suggerimenti.
	10. Una volta trovata l'espansione desiderata è necessario farci click dal menù a tendina, l'espansione è stata scelta correttamente se il tasto "Get all listings for current expansion" diventa interagibile e cliccabile.
	11. Fare click sul pulsante "Get all listings for current expansion".
	12. Fare click sul punsante "Start Process".	
	13. Il ciclo verrà avviato e sotto al pulsante "Start process" verranno visualizzate le inserzioni che il sw sta inserendo nel carrello, il processo terminerà nonappena verranno ciclate tutte le carte della espansione oppure 		verrà superato il massimo ammontare inseribile nel carrello.
	14. <ancora non completamente funzionante> In caso si voglia interrompere il processo, fare click su "Stop process"
