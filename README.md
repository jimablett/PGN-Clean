# PGN-Clean
Gui tool to clean/normalize and process a pgn file



This program uses the following great pgn tools:

1.  PGN-Extract by David J Barnes         :    https://www.cs.kent.ac.uk/people/staff/djb/pgn-extract/
2.  40-H Tools by Norm Pollock            :    http://www.nk-qy.info/40h/  
3.  Joined by Andreas Stabel              :    https://drive.proton.me/urls/M05YY4SNDG#I4htQjlkrQPM
4.  PGN Manager by Eduardo Suastegui      :    https://www.enpassant.dk/chess/softeng.htm
5.  Analyse-PGN by Jubai Mordecai Velasco :    https://github.com/mrdcvlsc/analyse-pgn
6.  Ordo by Miguel A. Ballicora           :    https://github.com/michiguel/Ordo




                     PGN-Clean by Jim Ablett
               ------------------------------------
      
	      To clean/normalize and process a pgn file
         These are the steps which are done automatically
       
	   --------------------------   CLEAN   ------------------------
       
	    Step  1:  Backup original pgn file
        
		Step  2: 'Trim'             to correctly re-format pgn file
        Step  3: 'PgnMan'           to remove duplicates
        Step  4: 'Joined'           to remove errors
        Step  5: 'Pgn-Extract'      to fix errors
        Step  6: 'tagFix'           to fix tag errors
        Step  7: 'tagOrder'         to put tags in the correct order
        Step  8: 'plyCount'         to add ply count tag
        Step  9: 'cleanUp'          to fix errors in the tag section
        Step 10: 'PgnMan'           to add ECO to openings
        Step 11: 'gameNum'          inserts consecutive 'game numbers
      
	  --------------------------   STATS   --------------------------
		
        Step 12: 'resultList'       to produce a crosstable of games
        Step 13: 'Summary'          to produce a summary stats file
        
        ------  If  'Create Extra Stats'  checkbox is ticked  -------
       
	   Step 14: 'Ordo'             to produce an ELO ratings list
        Step 15: 'NameList'         to produce player stats file
        Step 16: 'clusterList'      to list player clusters
        Step 17: 'colorList'        to list player results by colour
        Step 18: 'EcoList'          to produce an ECO stats file
        Step 19: 'resultSplit'      to produce PGNs based on results
		
		----------------------   EXTRA STATS   ----------------------
        
		--- If  'Create Extra Stats + Analysis PGN'  checkbox is ticked  
        
		Step 20: 'Apgn'             to produce an analysis PGN and stats   
        
		
		Processed files will be found in the 'OUTPUT' folder



Python script version requires the following installed:

pip install tk
pip install tqdm
pip install py7zr
pip install requests

