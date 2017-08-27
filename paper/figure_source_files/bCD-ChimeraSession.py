import cPickle, base64
try:
	from SimpleSession.versions.v65 import beginRestore,\
	    registerAfterModelsCB, reportRestoreError, checkVersion
except ImportError:
	from chimera import UserError
	raise UserError('Cannot open session that was saved in a'
	    ' newer version of Chimera; update your version')
checkVersion([1, 11, 2, 41380])
import chimera
from chimera import replyobj
replyobj.status('Restoring session...', \
    blankAfter=0)
replyobj.status('Beginning session restore...', \
    blankAfter=0, secondary=True)
beginRestore()

def restoreCoreModels():
	from SimpleSession.versions.v65 import init, restoreViewer, \
	     restoreMolecules, restoreColors, restoreSurfaces, \
	     restoreVRML, restorePseudoBondGroups, restoreModelAssociations
	molInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVRFyaWJib25JbnNpZGVDb2xvcnECSwJOfYdVCWJhbGxTY2FsZXEDSwJHP9AAAAAAAAB9h1UJcG9pbnRTaXplcQRLAkc/8AAAAAAAAH2HVQVjb2xvcnEFSwJLAH1xBksBXXEHSwFhc4dVCnJpYmJvblR5cGVxCEsCSwB9h1UKc3RpY2tTY2FsZXEJSwJHP/AAAAAAAAB9h1UMbW1DSUZIZWFkZXJzcQpdcQsoTk5lVQxhcm9tYXRpY01vZGVxDEsCSwF9h1UKdmR3RGVuc2l0eXENSwJHQBQAAAAAAAB9h1UGaGlkZGVucQ5LAol9h1UNYXJvbWF0aWNDb2xvcnEPSwJOfYdVD3JpYmJvblNtb290aGluZ3EQSwJLAH2HVQlhdXRvY2hhaW5xEUsCiH2HVQpwZGJWZXJzaW9ucRJLAksAfYdVCG9wdGlvbmFscRN9VQ9sb3dlckNhc2VDaGFpbnNxFEsCiX2HVQlsaW5lV2lkdGhxFUsCRz/wAAAAAAAAfYdVD3Jlc2lkdWVMYWJlbFBvc3EWSwJLAH2HVQRuYW1lcRdLAlgIAAAAdmFjLmNyZHN9h1UPYXJvbWF0aWNEaXNwbGF5cRhLAol9h1UPcmliYm9uU3RpZmZuZXNzcRlLAkc/6ZmZmZmZmn2HVQpwZGJIZWFkZXJzcRpdcRsofXEcfXEdZVUDaWRzcR5LAksBSwCGfXEfSwBLAIZdcSBLAGFzh1UOc3VyZmFjZU9wYWNpdHlxIUsCR7/wAAAAAAAAfYdVEGFyb21hdGljTGluZVR5cGVxIksCSwJ9h1UUcmliYm9uSGlkZXNNYWluY2hhaW5xI0sCiH2HVQdkaXNwbGF5cSRLAoh9h3Uu'))
	resInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQZpbnNlcnRxAksOVQEgfYdVC2ZpbGxEaXNwbGF5cQNLDol9h1UEbmFtZXEESw5YAwAAAE1HT32HVQVjaGFpbnEFSw5YAQAAAEF9h1UOcmliYm9uRHJhd01vZGVxBksOSwJ9h1UCc3NxB0sOiYmGfYdVCG1vbGVjdWxlcQhLDksAfXEJSwFOXXEKSwdLB4ZxC2GGc4dVC3JpYmJvbkNvbG9ycQxLDk59h1UFbGFiZWxxDUsOWAAAAAB9h1UKbGFiZWxDb2xvcnEOSw5OfYdVCGZpbGxNb2RlcQ9LDksBfYdVBWlzSGV0cRBLDol9h1ULbGFiZWxPZmZzZXRxEUsOTn2HVQhwb3NpdGlvbnESXXETKEsESweGcRRLBEsHhnEVZVUNcmliYm9uRGlzcGxheXEWSw6JfYdVCG9wdGlvbmFscRd9VQRzc0lkcRhLDkr/////fYd1Lg=='))
	atomInfo = cPickle.loads(base64.b64decode('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'))
	bondInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQVjb2xvcnECS+5OfXEDSwVdcQQoS6dLqEupS6pLq0usS61LrkuvS7BLsUuyS7NLtEu1S7ZLt0u4S7lLuku7S7xLvUu+S79LwEvBS8JLw0vES8VLxkvHS8hLyUvKS8tLzEvNS85Lz0vQS9FL0kvTS9RL1UvWS9dL2EvZS9pL20vcS91L3kvfS+BL4UviS+NL5EvlS+ZL50voS+lL6kvrS+xL7WVzh1UFYXRvbXNxBV1xBihdcQcoSyBLI2VdcQgoSx1LH2VdcQkoSx1LIGVdcQooSxtLHWVdcQsoSxtLkGVdcQwoSxdLGWVdcQ0oSxdLG2VdcQ4oSxNLFWVdcQ8oSxNLF2VdcRAoSxJLMGVdcREoSxBLEmVdcRIoSxBLE2VdcRMoSxBLH2VdcRQoSzVLOGVdcRUoSzJLNGVdcRYoSzJLNWVdcRcoSzBLMmVdcRgoSyxLLmVdcRkoSyxLMGVdcRooSyhLKmVdcRsoSyhLLGVdcRwoSydLRWVdcR0oSyVLJ2VdcR4oSyVLKGVdcR8oSyVLNGVdcSAoS0pLTWVdcSEoS0dLSWVdcSIoS0dLSmVdcSMoS0VLR2VdcSQoS0FLQ2VdcSUoS0FLRWVdcSYoSz1LP2VdcScoSz1LQWVdcSgoSzxLWmVdcSkoSzpLPGVdcSooSzpLPWVdcSsoSzpLSWVdcSwoS19LYmVdcS0oS1xLXmVdcS4oS1xLX2VdcS8oS1pLXGVdcTAoS1ZLWGVdcTEoS1ZLWmVdcTIoS1JLVGVdcTMoS1JLVmVdcTQoS1FLb2VdcTUoS09LUWVdcTYoS09LUmVdcTcoS09LXmVdcTgoS3RLd2VdcTkoS3FLc2VdcTooS3FLdGVdcTsoS29LcWVdcTwoS2tLbWVdcT0oS2tLb2VdcT4oS2dLaWVdcT8oS2dLa2VdcUAoS2ZLhGVdcUEoS2RLZmVdcUIoS2RLZ2VdcUMoS2RLc2VdcUQoS4lLjGVdcUUoS4ZLiGVdcUYoS4ZLiWVdcUcoS4RLhmVdcUgoS4BLgmVdcUkoS4BLhGVdcUooS3xLfmVdcUsoS3xLgGVdcUwoS3tLmWVdcU0oS3lLe2VdcU4oS3lLfGVdcU8oS3lLiGVdcVAoS55LoWVdcVEoS5tLnWVdcVIoS5tLnmVdcVMoS5lLm2VdcVQoS5VLl2VdcVUoS5VLmWVdcVYoS5FLk2VdcVcoS5FLlWVdcVgoS45LkGVdcVkoS45LkWVdcVooS45LnWVdcVsoSyNLJGVdcVwoSyBLIWVdcV0oSyBLImVdcV4oSx1LHmVdcV8oSxtLHGVdcWAoSxlLGmVdcWEoSxdLGGVdcWIoSxVLFmVdcWMoSxNLFGVdcWQoSxBLEWVdcWUoSzhLOWVdcWYoSzVLNmVdcWcoSzVLN2VdcWgoSzJLM2VdcWkoSzBLMWVdcWooSy5LL2VdcWsoSyxLLWVdcWwoSypLK2VdcW0oSyhLKWVdcW4oSyVLJmVdcW8oS01LTmVdcXAoS0pLS2VdcXEoS0pLTGVdcXIoS0dLSGVdcXMoS0VLRmVdcXQoS0NLRGVdcXUoS0FLQmVdcXYoSz9LQGVdcXcoSz1LPmVdcXgoSzpLO2VdcXkoS2JLY2VdcXooS19LYGVdcXsoS19LYWVdcXwoS1xLXWVdcX0oS1pLW2VdcX4oS1hLWWVdcX8oS1ZLV2VdcYAoS1RLVWVdcYEoS1JLU2VdcYIoS09LUGVdcYMoS3dLeGVdcYQoS3RLdWVdcYUoS3RLdmVdcYYoS3FLcmVdcYcoS29LcGVdcYgoS21LbmVdcYkoS2tLbGVdcYooS2lLamVdcYsoS2dLaGVdcYwoS2RLZWVdcY0oS4xLjWVdcY4oS4lLimVdcY8oS4lLi2VdcZAoS4ZLh2VdcZEoS4RLhWVdcZIoS4JLg2VdcZMoS4BLgWVdcZQoS35Lf2VdcZUoS3xLfWVdcZYoS3lLemVdcZcoS6FLomVdcZgoS55Ln2VdcZkoS55LoGVdcZooS5tLnGVdcZsoS5lLmmVdcZwoS5dLmGVdcZ0oS5VLlmVdcZ4oS5NLlGVdcZ8oS5FLkmVdcaAoS45Lj2VdcaEoS6xLrWVdcaIoS6pLq2VdcaMoS6pLrGVdcaQoS6lLqmVdcaUoS6lL5mVdcaYoS6dLqGVdcacoS6dLqWVdcagoS6VLpmVdcakoS6VLp2VdcaooS6RLtGVdcasoS6NLpGVdcawoS6NLpWVdca0oS6NLq2Vdca4oS7dLuGVdca8oS7VLtmVdcbAoS7VLt2VdcbEoS7RLtWVdcbIoS7JLs2VdcbMoS7JLtGVdcbQoS7BLsWVdcbUoS7BLsmVdcbYoS69Lv2VdcbcoS65Lr2VdcbgoS65LsGVdcbkoS65LtmVdcbooS8JLw2VdcbsoS8BLwWVdcbwoS8BLwmVdcb0oS79LwGVdcb4oS71LvmVdcb8oS71Lv2VdccAoS7tLvGVdccEoS7tLvWVdccIoS7pLymVdccMoS7lLumVdccQoS7lLu2VdccUoS7lLwWVdccYoS81LzmVdcccoS8tLzGVdccgoS8tLzWVdcckoS8pLy2VdccooS8hLyWVdccsoS8hLymVdccwoS8ZLx2Vdcc0oS8ZLyGVdcc4oS8VL1WVdcc8oS8RLxWVdcdAoS8RLxmVdcdEoS8RLzGVdcdIoS9hL2WVdcdMoS9ZL12VdcdQoS9ZL2GVdcdUoS9VL1mVdcdYoS9NL1GVdcdcoS9NL1WVdcdgoS9FL0mVdcdkoS9FL02VdcdooS9BL4GVdcdsoS89L0GVdcdwoS89L0WVdcd0oS89L12Vdcd4oS+NL5GVdcd8oS+FL4mVdceAoS+FL42VdceEoS+BL4WVdceIoS95L32VdceMoS95L4GVdceQoS9xL3WVdceUoS9xL3mVdceYoS9tL62VdcecoS9pL22VdcegoS9pL3GVdcekoS9pL4mVdceooS+5L72VdcesoS+xL7WVdcewoS+xL7mVdce0oS+tL7GVdce4oS+lL6mVdce8oS+lL62VdcfAoS+dL6GVdcfEoS+dL6WVdcfIoS+VL5mVdcfMoS+VL52VdcfQoS+VL7WVlVQVsYWJlbHH1S+5YAAAAAH2HVQhoYWxmYm9uZHH2S+6IfYdVBnJhZGl1c3H3S+5HP8mZmaAAAAB9h1ULbGFiZWxPZmZzZXRx+EvuTn2HVQhkcmF3TW9kZXH5S+5LAX2HVQhvcHRpb25hbHH6fVUHZGlzcGxheXH7S+5LAn2HdS4='))
	crdInfo = cPickle.loads(base64.b64decode('gAJ9cQEoSwB9cQIoVQZhY3RpdmVxA0sBSwFdcQQoRwAAAAAAAAAARwAAAAAAAAAAR8AYAAAAAAAAh3EFRwAAAAAAAAAARwAAAAAAAAAAR8AmAAAAAAAAh3EGRwAAAAAAAAAAR0AMAAAAAAAAR8AtAAAAAAAAh3EHR8ARwIMSbpeNR8AROFHrhR64R0AD3ztkWhysh3EIR8AWGJN0vGp/R8AR6n752yLRR0AC1wo9cKPXh3EJR8AQmp++dsi0R8AHLQ5WBBiTR0AGS8an752yh3EKR8APpeNT987ZR8AUqfvnbItER0ANLxqfvnbJh3ELR8AQ2hysCDEnR8AY2RaHKwIMR0ALtkWhysCDh3EMR8ASTdLxqfvnR8AS5WBBiTdMR0ATeNT987ZGh3ENR8ATv3ztkWhzR8AOo9cKPXCkR0ATAgxJul41h3EOR8ADrhR64UeuR8AUGJN0vGp/R0AOsi0OVgQZh3EPR8AByLQ5WBBiR8AP++dsi0OWR0AQhysCDEm6h3EQR8AAsCDEm6XjR8AXzMzMzMzNR0ATe+dsi0OWh3ERR8AGan752yLRR8AXvGp++dsjR0AWFYEGJN0vh3ESR7/7tkWhysCDR8AVhiTdLxqgR0AEaHKwIMSch3ETR7/+IMSbpeNUR8AZxJul41P4R0ACtkWhysCDh3EUR8AB9cKPXCj2R8ASKwIMSbpeRz/164UeuFHsh3EVR8AAU/fO2RaHR8AL752yLQ5WRz/5eNT987ZGh3EWR8ANvnbItDlYR8AS2BBiTdLyRz/0LQ5WBBiTh3EXR7/5vnbItDlYR8ATRqfvnbItR79QYk3S8an8h3EYR7/nU/fO2RaHR8AQvXCj1wo9R7/A5WBBiTdMh3EZR8ACi0OVgQYlR8ASVwo9cKPXR7/pgQYk3S8bh3EaR7/zP3ztkWhzR8AYwo9cKPXDR7+7ItDlYEGJh3EbR7/S4UeuFHrhR8AZC0OVgQYlRz/LhR64UeuFh3EcR8AYiDEm6XjVRz/pHrhR64UfR0AD4UeuFHrhh3EdR8AbyLQ5WBBiRz/4an752yLRR0AC2yLQ5WBCh3EeR8ATaXjU/fO2Rz/3BiTdLxqgR0AGTdLxqfvnh3EfR8AaBR64UeuFR7/AYk3S8an8R0ANMzMzMzMzh3EgR8Ad752yLQ5WR7/ihysCDEm6R0ALuFHrhR64h3EhR8AaLhR64UeuRz/kMSbpeNT+R0ATeNT987ZGh3EiR8AYSbpeNT99Rz/3jU/fO2RaR0ATAxJul41Qh3EjR8AV2BBiTdLyR7/zWBBiTdLyR0AOsi0OVgQZh3EkR8ASC0OVgQYlR7/oKPXCj1wpR0AQhysCDEm6h3ElR8AXztkWhysCR8AAocrAgxJvR0ATeuFHrhR7h3EmR8AZi0OVgQYlR7/4KPXCj1wpR0AWFocrAgxKh3EnR8AVJN0vGp++R8AAAgxJul41R0AEaHKwIMSch3EoR8AY2BBiTdLyR8AEXCj1wo9cR0ACtkWhysCDh3EpR8ATzdLxqfvnR7/xP3ztkWhzRz/164UeuFHsh3EqR8AQBBiTdLxqR7/in752yLQ5Rz/5fO2RaHKwh3ErR8AYAgxJul41R7+euFHrhR64Rz/0MSbpeNT+h3EsR8ATFYEGJN0vR7/7752yLQ5WRwAAAAAAAAAAh3EtR8AN0OVgQYk3R8AATdLxqfvnR7/BBiTdLxqgh3EuR8AUHrhR64UfR7/wuFHrhR64R7/pgQYk3S8bh3EvR8AWXS8an753R8AHWBBiTdLyR7+7ItDlYEGJh3EwR8AUUeuFHrhSR8ANYk3S8an8Rz/LhR64UeuFh3ExR8AJrhR64UeuR0AVI9cKPXCkR0AD41P3ztkXh3EyR8AJGJN0vGp/R0AZhysCDEm6R0AC2yLQ5WBCh3EzR7/+an752yLRR0ASw5WBBiTdR0AGTdLxqfvnh3E0R8AQnrhR64UfR0AUBiTdLxqgR0ANMzMzMzMzh3E1R8AUedsi0OVgR0AV9cKPXCj2R0ALul41P3zuh3E2R8AMsCDEm6XjR0AWC0OVgQYlR0ATedsi0OVgh3E3R8AFFHrhR64UR0AWqPXCj1wpR0ATAxJul41Qh3E4R8ARZmZmZmZmR0AMHrhR64UfR0AOtDlYEGJOh3E5R8ALN0vGp++eR0AIcrAgxJumR0AQiDEm6XjVh3E6R8AVWBBiTdLyR0AK2yLQ5WBCR0ATe+dsi0OWh3E7R8AUo9cKPXCkR0AQNDlYEGJOR0AWF41P3ztkh3E8R8ATcan752yLR0AHFocrAgxKR0AEan752yLRh3E9R8AXcrAgxJumR0AKKPXCj1wpR0ACuFHrhR64h3E+R8APcrAgxJumR0AJmZmZmZmaRz/1752yLQ5Wh3E/R8AHnbItDlYER0AGJN0vGp++Rz/5fO2RaHKwh3FAR8AOIMSbpeNUR0ASsi0OVgQZRz/0NT987ZFoh3FBR8ARXS8an753R0AFItDlYEGJRz9QYk3S8an8h3FCR8APWhysCDEnRz/6TdLxqfvnR7/A5WBBiTdMh3FDR8APo9cKPXCkR0AKQYk3S8aoR7/pgQYk3S8bh3FER8AXE3S8an76R0AEan752yLRR7+64UeuFHrhh3FFR8AYJ++dsi0ORz/66XjU/fO2Rz/LpeNT987Zh3FGR0ABDEm6XjU/R0AXOFHrhR64R0AD3ztkWhysh3FHR0AIRaHKwIMSR0AZul41P3zuR0AC2RaHKwIMh3FIR0AD2RaHKwIMR0ARpN0vGp++R0AGS8an752yh3FJRz/1KwIMSbpeR0AZeuFHrhR7R0ANMSbpeNT+h3FKRz/xnbItDlYER0AdszMzMzMzR0ALtkWhysCDh3FLR0AAlYEGJN0vR0AY9si0OVgQR0ATeNT987ZGh3FMR0AGS8an752yR0AWXztkWhysR0ATAgxJul41h3FNRz+i8an752yLR0AWXztkWhysR0AOsi0OVgQZh3FORz/RJul41P30R0ASQ5WBBiTdR0AQiDEm6XjVh3FPR7/mdsi0OVgQR0AZD1wo9cKPR0ATeuFHrhR7h3FQR7+pmZmZmZmaR0AaPnbItDlYR0AWFYEGJN0vh3FRR7/ozMzMzMzNR0AWZWBBiTdMR0AEan752yLRh3FSR7/xkWhysCDFR0Aae+dsi0OWR0ACtkWhysCDh3FTRz+qHKwIMSbpR0AURJul41P4Rz/1752yLQ5Wh3FURz/UvGp++dsjR0AQIcrAgxJvRz/5fO2RaHKwh3FVRz/05WBBiTdMR0AXbpeNT987Rz/0MSbpeNT+h3FWR7/ki0OVgQYlR0AUKfvnbItERwAAAAAAAAAAh3FXR7/yi0OVgQYlR0AQWRaHKwIMR7/A5WBBiTdMh3FYRz+5WBBiTdLyR0AUjEm6XjU/R7/pgQYk3S8bh3FZR7/5ocrAgxJvR0AYZWBBiTdMR7+64UeuFHrhh3FaR8ADm6XjU/fPR0AXFHrhR64URz/LxqfvnbIth3FbR0AXdsi0OVgQRz//Q5WBBiTdR0AD3ztkWhysh3FcR0AbrhR64UeuRz/6OVgQYk3TR0AC1P3ztkWih3FdR0AT++dsi0OWRz/p64UeuFHsR0AGS8an752yh3FeR0AXOFHrhR64R0AHgQYk3S8bR0ANLxqfvnbJh3FfR0AZ987ZFocrR0AOJul41P30R0ALtDlYEGJOh3FgR0AYsCDEm6XjR0ACKwIMSbpeR0ATd87ZFocrh3FhR0AYcKPXCj1xRz/08an752yLR0ATAgxJul41h3FiR0ARlYEGJN0vR0ALrhR64UeuR0AOsCDEm6Xjh3FjR0AN5WBBiTdMR0AFGp++dsi0R0AQhysCDEm6h3FkR0AR1wo9cKPXR0AR0vGp++dtR0ATeuFHrhR7h3FlR0AUZFocrAgxR0AQhiTdLxqgR0AWFHrhR64Uh3FmR0APKPXCj1wpR0AQY1P3ztkXR0AEaHKwIMSch3FnR0AR987ZFocrR0AT87ZFocrBR0ACtDlYEGJOh3FoR0AP752yLQ5WR0AI87ZFocrBRz/164UeuFHsh3FpR0AK1wo9cKPXR0ACFocrAgxKRz/5fO2RaHKwh3FqR0AVk3S8an76R0AFDlYEGJN1Rz/0LQ5WBBiTh3FrR0AMUeuFHrhSR0ANJN0vGp++R79QYk3S8an8h3FsR0ADxqfvnbItR0ALocrAgxJvR7/BBiTdLxqgh3FtR0AQTtkWhysCR0AJAAAAAAAAR7/piTdLxqfwh3FuR0AOKPXCj1wpR0AUOFHrhR64R7+7ZFocrAgxh3FvR0AH2yLQ5WBCR0AWDU/fO2RaRz/LpeNT987Zh3FwR0AUvXCj1wo9R8AK87ZFocrBR0AD4UeuFHrhh3FxR0AWY1P3ztkXR8ARjlYEGJN1R0AC2yLQ5WBCh3FyR0AN++dsi0OWR8ALN0vGp++eR0AGS8an752yh3FzR0AXqwIMSbpeR8AFp++dsi0OR0ANMSbpeNT+h3F0R0Ab+dsi0OVgR8AFzMzMzMzNR0ALuFHrhR64h3F1R0AWffO2RaHLR8ALRaHKwIMSR0ATeNT987ZGh3F2R0ATVP3ztkWiR8APsCDEm6XjR0ATAxJul41Qh3F3R0AVx64UeuFIR7/0euFHrhR7R0AOtDlYEGJOh3F4R0ARkWhysCDFR7/0bpeNT987R0AQiDEm6XjVh3F5R0AZDlYEGJN1R7/msCDEm6XjR0ATe+dsi0OWh3F6R0AZocrAgxJvR7/2j1wo9cKPR0AWFocrAgxKh3F7R0AWhysCDEm6R7/fbItDlYEGR0AEaHKwIMSch3F8R0AazMzMzMzNR7/Zul41P3zuR0ACtkWhysCDh3F9R0ATtkWhysCDR7/y2RaHKwIMRz/1752yLQ5Wh3F+R0AO41P3ztkXR7/zaHKwIMScRz/5eNT987ZGh3F/R0AVrxqfvnbJR8AEnbItDlYERz/0MSbpeNT+h3GAR0AUOl41P3zuR7/fztkWhysCRwAAAAAAAAAAh3GBR0AQ+NT987ZGRz/MCDEm6XjVR7/BBiTdLxqgh3GCR0AT8rAgxJumR7/z3ztkWhysR7/pgQYk3S8bh3GDR0AZN0vGp++eRz/J++dsi0OWR7+7ItDlYEGJh3GER0AYrxqfvnbJRz/xrhR64UeuRz/LhR64UeuFh3GFRz/jKwIMSbpeR8AYnbItDlYER0AD4UeuFHrhh3GGRz+tLxqfvnbJR8Accan752yLR0AC2RaHKwIMh3GHR7/Um6XjU/fPR8AUNDlYEGJOR0AGS8an752yh3GIRz/5Jul41P30R8AZQYk3S8aoR0ANMzMzMzMzh3GJR0AB1wo9cKPXR8AcqwIMSbpeR0ALuFHrhR64h3GKRz/q4UeuFHrhR8AaFYEGJN0vR0ATeNT987ZGh3GLR7+1gQYk3S8bR8AY/fO2RaHLR0ATAxJul41Qh3GMR0ADJul41P30R8AUOFHrhR64R0AOtDlYEGJOh3GNRz/71wo9cKPXR8AQ64UeuFHsR0AQiDEm6XjVh3GOR0AKztkWhysCR8AVXCj1wo9cR0ATfO2RaHKwh3GPR0AHItDlYEGJR8AXjlYEGJN1R0AWFocrAgxKh3GQR0AJBiTdLxqgR8AS1P3ztkWiR0AEan752yLRh3GRR0AO52yLQ5WBR8AV9LxqfvnbR0ACuFHrhR64h3GSR0ABOVgQYk3TR8ASWRaHKwIMRz/164UeuFHsh3GTRz/3U/fO2RaHR8AOMSbpeNT+Rz/5fO2RaHKwh3GURz/12yLQ5WBCR8AXYUeuFHrhRz/0NT987ZFoh3GVR0AGHrhR64UfR8ARDU/fO2RaRwAAAAAAAAAAh3GWR0AGi0OVgQYlR8AJcrAgxJumR7/BBiTdLxqgh3GXR0ABHrhR64UfR8ASsCDEm6XjR7/pgQYk3S8bh3GYR0AQXCj1wo9cR8ATNT987ZFoR7+64UeuFHrhh3GZR0AS2RaHKwIMR8AQi0OVgQYlRz/LxqfvnbIth3GaZXVLAX1xmyhoA0sBSwFdcZwoRwAAAAAAAAAARwAAAAAAAAAAR8AYAAAAAAAAh3GdRwAAAAAAAAAARwAAAAAAAAAAR8AmAAAAAAAAh3GeRwAAAAAAAAAAR0AMAAAAAAAAR8AtAAAAAAAAh3GfR8ARwIMSbpeNR8AROFHrhR64R0AD3ztkWhysh3GgR8AWGJN0vGp/R8AR6n752yLRR0AC1wo9cKPXh3GhR8AQmp++dsi0R8AHLQ5WBBiTR0AGS8an752yh3GiR8APpeNT987ZR8AUqfvnbItER0ANLxqfvnbJh3GjR8AQ2hysCDEnR8AY2RaHKwIMR0ALtkWhysCDh3GkR8ASTdLxqfvnR8AS5WBBiTdMR0ATeNT987ZGh3GlR8ATv3ztkWhzR8AOo9cKPXCkR0ATAgxJul41h3GmR8ADrhR64UeuR8AUGJN0vGp/R0AOsi0OVgQZh3GnR8AByLQ5WBBiR8AP++dsi0OWR0AQhysCDEm6h3GoR8AAsCDEm6XjR8AXzMzMzMzNR0ATe+dsi0OWh3GpR8AGan752yLRR8AXvGp++dsjR0AWFYEGJN0vh3GqR7/7tkWhysCDR8AVhiTdLxqgR0AEaHKwIMSch3GrR7/+IMSbpeNUR8AZxJul41P4R0ACtkWhysCDh3GsR8AB9cKPXCj2R8ASKwIMSbpeRz/164UeuFHsh3GtR8AAU/fO2RaHR8AL752yLQ5WRz/5eNT987ZGh3GuR8ANvnbItDlYR8AS2BBiTdLyRz/0LQ5WBBiTh3GvR7/5vnbItDlYR8ATRqfvnbItR79QYk3S8an8h3GwR7/nU/fO2RaHR8AQvXCj1wo9R7/A5WBBiTdMh3GxR8ACi0OVgQYlR8ASVwo9cKPXR7/pgQYk3S8bh3GyR7/zP3ztkWhzR8AYwo9cKPXDR7+7ItDlYEGJh3GzR7/S4UeuFHrhR8AZC0OVgQYlRz/LhR64UeuFh3G0R8AYiDEm6XjVRz/pHrhR64UfR0AD4UeuFHrhh3G1R8AbyLQ5WBBiRz/4an752yLRR0AC2yLQ5WBCh3G2R8ATaXjU/fO2Rz/3BiTdLxqgR0AGTdLxqfvnh3G3R8AaBR64UeuFR7/AYk3S8an8R0ANMzMzMzMzh3G4R8Ad752yLQ5WR7/ihysCDEm6R0ALuFHrhR64h3G5R8AaLhR64UeuRz/kMSbpeNT+R0ATeNT987ZGh3G6R8AYSbpeNT99Rz/3jU/fO2RaR0ATAxJul41Qh3G7R8AV2BBiTdLyR7/zWBBiTdLyR0AOsi0OVgQZh3G8R8ASC0OVgQYlR7/oKPXCj1wpR0AQhysCDEm6h3G9R8AXztkWhysCR8AAocrAgxJvR0ATeuFHrhR7h3G+R8AZi0OVgQYlR7/4KPXCj1wpR0AWFocrAgxKh3G/R8AVJN0vGp++R8AAAgxJul41R0AEaHKwIMSch3HAR8AY2BBiTdLyR8AEXCj1wo9cR0ACtkWhysCDh3HBR8ATzdLxqfvnR7/xP3ztkWhzRz/164UeuFHsh3HCR8AQBBiTdLxqR7/in752yLQ5Rz/5fO2RaHKwh3HDR8AYAgxJul41R7+euFHrhR64Rz/0MSbpeNT+h3HER8ATFYEGJN0vR7/7752yLQ5WRwAAAAAAAAAAh3HFR8AN0OVgQYk3R8AATdLxqfvnR7/BBiTdLxqgh3HGR8AUHrhR64UfR7/wuFHrhR64R7/pgQYk3S8bh3HHR8AWXS8an753R8AHWBBiTdLyR7+7ItDlYEGJh3HIR8AUUeuFHrhSR8ANYk3S8an8Rz/LhR64UeuFh3HJR8AJrhR64UeuR0AVI9cKPXCkR0AD41P3ztkXh3HKR8AJGJN0vGp/R0AZhysCDEm6R0AC2yLQ5WBCh3HLR7/+an752yLRR0ASw5WBBiTdR0AGTdLxqfvnh3HMR8AQnrhR64UfR0AUBiTdLxqgR0ANMzMzMzMzh3HNR8AUedsi0OVgR0AV9cKPXCj2R0ALul41P3zuh3HOR8AMsCDEm6XjR0AWC0OVgQYlR0ATedsi0OVgh3HPR8AFFHrhR64UR0AWqPXCj1wpR0ATAxJul41Qh3HQR8ARZmZmZmZmR0AMHrhR64UfR0AOtDlYEGJOh3HRR8ALN0vGp++eR0AIcrAgxJumR0AQiDEm6XjVh3HSR8AVWBBiTdLyR0AK2yLQ5WBCR0ATe+dsi0OWh3HTR8AUo9cKPXCkR0AQNDlYEGJOR0AWF41P3ztkh3HUR8ATcan752yLR0AHFocrAgxKR0AEan752yLRh3HVR8AXcrAgxJumR0AKKPXCj1wpR0ACuFHrhR64h3HWR8APcrAgxJumR0AJmZmZmZmaRz/1752yLQ5Wh3HXR8AHnbItDlYER0AGJN0vGp++Rz/5fO2RaHKwh3HYR8AOIMSbpeNUR0ASsi0OVgQZRz/0NT987ZFoh3HZR8ARXS8an753R0AFItDlYEGJRz9QYk3S8an8h3HaR8APWhysCDEnRz/6TdLxqfvnR7/A5WBBiTdMh3HbR8APo9cKPXCkR0AKQYk3S8aoR7/pgQYk3S8bh3HcR8AXE3S8an76R0AEan752yLRR7+64UeuFHrhh3HdR8AYJ++dsi0ORz/66XjU/fO2Rz/LpeNT987Zh3HeR0ABDEm6XjU/R0AXOFHrhR64R0AD3ztkWhysh3HfR0AIRaHKwIMSR0AZul41P3zuR0AC2RaHKwIMh3HgR0AD2RaHKwIMR0ARpN0vGp++R0AGS8an752yh3HhRz/1KwIMSbpeR0AZeuFHrhR7R0ANMSbpeNT+h3HiRz/xnbItDlYER0AdszMzMzMzR0ALtkWhysCDh3HjR0AAlYEGJN0vR0AY9si0OVgQR0ATeNT987ZGh3HkR0AGS8an752yR0AWXztkWhysR0ATAgxJul41h3HlRz+i8an752yLR0AWXztkWhysR0AOsi0OVgQZh3HmRz/RJul41P30R0ASQ5WBBiTdR0AQiDEm6XjVh3HnR7/mdsi0OVgQR0AZD1wo9cKPR0ATeuFHrhR7h3HoR7+pmZmZmZmaR0AaPnbItDlYR0AWFYEGJN0vh3HpR7/ozMzMzMzNR0AWZWBBiTdMR0AEan752yLRh3HqR7/xkWhysCDFR0Aae+dsi0OWR0ACtkWhysCDh3HrRz+qHKwIMSbpR0AURJul41P4Rz/1752yLQ5Wh3HsRz/UvGp++dsjR0AQIcrAgxJvRz/5fO2RaHKwh3HtRz/05WBBiTdMR0AXbpeNT987Rz/0MSbpeNT+h3HuR7/ki0OVgQYlR0AUKfvnbItERwAAAAAAAAAAh3HvR7/yi0OVgQYlR0AQWRaHKwIMR7/A5WBBiTdMh3HwRz+5WBBiTdLyR0AUjEm6XjU/R7/pgQYk3S8bh3HxR7/5ocrAgxJvR0AYZWBBiTdMR7+64UeuFHrhh3HyR8ADm6XjU/fPR0AXFHrhR64URz/LxqfvnbIth3HzR0AXdsi0OVgQRz//Q5WBBiTdR0AD3ztkWhysh3H0R0AbrhR64UeuRz/6OVgQYk3TR0AC1P3ztkWih3H1R0AT++dsi0OWRz/p64UeuFHsR0AGS8an752yh3H2R0AXOFHrhR64R0AHgQYk3S8bR0ANLxqfvnbJh3H3R0AZ987ZFocrR0AOJul41P30R0ALtDlYEGJOh3H4R0AYsCDEm6XjR0ACKwIMSbpeR0ATd87ZFocrh3H5R0AYcKPXCj1xRz/08an752yLR0ATAgxJul41h3H6R0ARlYEGJN0vR0ALrhR64UeuR0AOsCDEm6Xjh3H7R0AN5WBBiTdMR0AFGp++dsi0R0AQhysCDEm6h3H8R0AR1wo9cKPXR0AR0vGp++dtR0ATeuFHrhR7h3H9R0AUZFocrAgxR0AQhiTdLxqgR0AWFHrhR64Uh3H+R0APKPXCj1wpR0AQY1P3ztkXR0AEaHKwIMSch3H/R0AR987ZFocrR0AT87ZFocrBR0ACtDlYEGJOh3IAAQAAR0AP752yLQ5WR0AI87ZFocrBRz/164UeuFHsh3IBAQAAR0AK1wo9cKPXR0ACFocrAgxKRz/5fO2RaHKwh3ICAQAAR0AVk3S8an76R0AFDlYEGJN1Rz/0LQ5WBBiTh3IDAQAAR0AMUeuFHrhSR0ANJN0vGp++R79QYk3S8an8h3IEAQAAR0ADxqfvnbItR0ALocrAgxJvR7/BBiTdLxqgh3IFAQAAR0AQTtkWhysCR0AJAAAAAAAAR7/piTdLxqfwh3IGAQAAR0AOKPXCj1wpR0AUOFHrhR64R7+7ZFocrAgxh3IHAQAAR0AH2yLQ5WBCR0AWDU/fO2RaRz/LpeNT987Zh3IIAQAAR0AUvXCj1wo9R8AK87ZFocrBR0AD4UeuFHrhh3IJAQAAR0AWY1P3ztkXR8ARjlYEGJN1R0AC2yLQ5WBCh3IKAQAAR0AN++dsi0OWR8ALN0vGp++eR0AGS8an752yh3ILAQAAR0AXqwIMSbpeR8AFp++dsi0OR0ANMSbpeNT+h3IMAQAAR0Ab+dsi0OVgR8AFzMzMzMzNR0ALuFHrhR64h3INAQAAR0AWffO2RaHLR8ALRaHKwIMSR0ATeNT987ZGh3IOAQAAR0ATVP3ztkWiR8APsCDEm6XjR0ATAxJul41Qh3IPAQAAR0AVx64UeuFIR7/0euFHrhR7R0AOtDlYEGJOh3IQAQAAR0ARkWhysCDFR7/0bpeNT987R0AQiDEm6XjVh3IRAQAAR0AZDlYEGJN1R7/msCDEm6XjR0ATe+dsi0OWh3ISAQAAR0AZocrAgxJvR7/2j1wo9cKPR0AWFocrAgxKh3ITAQAAR0AWhysCDEm6R7/fbItDlYEGR0AEaHKwIMSch3IUAQAAR0AazMzMzMzNR7/Zul41P3zuR0ACtkWhysCDh3IVAQAAR0ATtkWhysCDR7/y2RaHKwIMRz/1752yLQ5Wh3IWAQAAR0AO41P3ztkXR7/zaHKwIMScRz/5eNT987ZGh3IXAQAAR0AVrxqfvnbJR8AEnbItDlYERz/0MSbpeNT+h3IYAQAAR0AUOl41P3zuR7/fztkWhysCRwAAAAAAAAAAh3IZAQAAR0AQ+NT987ZGRz/MCDEm6XjVR7/BBiTdLxqgh3IaAQAAR0AT8rAgxJumR7/z3ztkWhysR7/pgQYk3S8bh3IbAQAAR0AZN0vGp++eRz/J++dsi0OWR7+7ItDlYEGJh3IcAQAAR0AYrxqfvnbJRz/xrhR64UeuRz/LhR64UeuFh3IdAQAARz/jKwIMSbpeR8AYnbItDlYER0AD4UeuFHrhh3IeAQAARz+tLxqfvnbJR8Accan752yLR0AC2RaHKwIMh3IfAQAAR7/Um6XjU/fPR8AUNDlYEGJOR0AGS8an752yh3IgAQAARz/5Jul41P30R8AZQYk3S8aoR0ANMzMzMzMzh3IhAQAAR0AB1wo9cKPXR8AcqwIMSbpeR0ALuFHrhR64h3IiAQAARz/q4UeuFHrhR8AaFYEGJN0vR0ATeNT987ZGh3IjAQAAR7+1gQYk3S8bR8AY/fO2RaHLR0ATAxJul41Qh3IkAQAAR0ADJul41P30R8AUOFHrhR64R0AOtDlYEGJOh3IlAQAARz/71wo9cKPXR8AQ64UeuFHsR0AQiDEm6XjVh3ImAQAAR0AKztkWhysCR8AVXCj1wo9cR0ATfO2RaHKwh3InAQAAR0AHItDlYEGJR8AXjlYEGJN1R0AWFocrAgxKh3IoAQAAR0AJBiTdLxqgR8AS1P3ztkWiR0AEan752yLRh3IpAQAAR0AO52yLQ5WBR8AV9LxqfvnbR0ACuFHrhR64h3IqAQAAR0ABOVgQYk3TR8ASWRaHKwIMRz/164UeuFHsh3IrAQAARz/3U/fO2RaHR8AOMSbpeNT+Rz/5fO2RaHKwh3IsAQAARz/12yLQ5WBCR8AXYUeuFHrhRz/0NT987ZFoh3ItAQAAR0AGHrhR64UfR8ARDU/fO2RaRwAAAAAAAAAAh3IuAQAAR0AGi0OVgQYlR8AJcrAgxJumR7/BBiTdLxqgh3IvAQAAR0ABHrhR64UfR8ASsCDEm6XjR7/pgQYk3S8bh3IwAQAAR0AQXCj1wo9cR8ATNT987ZFoR7+64UeuFHrhh3IxAQAAR0AS2RaHKwIMR8AQi0OVgQYlRz/LxqfvnbIth3IyAQAAZXV1Lg=='))
	surfInfo = {'category': (1, u'main', {}), 'probeRadius': (1, 1.4, {}), 'pointSize': (1, 1, {}), 'name': [u'MSMS main surface of vac.crds'], 'density': (1, 20, {}), 'colorMode': (1, 1, {}), 'useLighting': (1, True, {}), 'transparencyBlendMode': (1, 1, {}), 'molecule': [0], 'smoothLines': (1, False, {}), 'lineWidth': (1, 1, {}), 'allComponents': (1, True, {}), 'twoSidedLighting': (1, True, {}), 'customVisibility': [None], 'drawMode': (1, 0, {}), 'display': (1, True, {}), 'customColors': [(0, None, {})]}
	vrmlInfo = {'subid': (0, None, {}), 'display': (0, None, {}), 'id': (0, None, {}), 'vrmlString': [], 'name': (0, None, {})}
	colors = {'Ru': ((0.141176, 0.560784, 0.560784), 1, u'default'), 'Re': ((0.14902, 0.490196, 0.670588), 1, u'default'), 'Rf': ((0.8, 0, 0.34902), 1, u'default'), 'Ra': ((0, 0.490196, 0), 1, u'default'), 'Rb': ((0.439216, 0.180392, 0.690196), 1, u'default'), 'Rn': ((0.258824, 0.509804, 0.588235), 1, u'default'), 'Rh': ((0.0392157, 0.490196, 0.54902), 1, u'default'), 'Be': ((0.760784, 1, 0), 1, u'default'), 'Ba': ((0, 0.788235, 0), 1, u'default'), 'Bh': ((0.878431, 0, 0.219608), 1, u'default'), 'Bi': ((0.619608, 0.309804, 0.709804), 1, u'default'), 'Bk': ((0.541176, 0.309804, 0.890196), 1, u'default'), 'Br': ((0.65098, 0.160784, 0.160784), 1, u'default'), 'H': ((1, 1, 1), 1, u'default'), 'P': ((1, 0.501961, 0), 1, u'default'), 'Os': ((0.14902, 0.4, 0.588235), 1, u'default'), 'Ge': ((0.4, 0.560784, 0.560784), 1, u'default'), 'Gd': ((0.270588, 1, 0.780392), 1, u'default'), 'Ga': ((0.760784, 0.560784, 0.560784), 1, u'default'), 'Pr': ((0.85098, 1, 0.780392), 1, u'default'), 'Pt': ((0.815686, 0.815686, 0.878431), 1, u'default'), 'Pu': ((0, 0.419608, 1), 1, u'default'),
'C': ((0.564706, 0.564706, 0.564706), 1, u'default'), 'Pb': ((0.341176, 0.34902, 0.380392), 1, u'default'), 'Pa': ((0, 0.631373, 1), 1, u'default'), 'Pd': ((0, 0.411765, 0.521569), 1, u'default'), 'Cd': ((1, 0.85098, 0.560784), 1, u'default'), 'Po': ((0.670588, 0.360784, 0), 1, u'default'), 'Pm': ((0.639216, 1, 0.780392), 1, u'default'), 'Hs': ((0.901961, 0, 0.180392), 1, u'default'), 'Ho': ((0, 1, 0.611765), 1, u'default'), 'Hf': ((0.301961, 0.760784, 1), 1, u'default'), 'Hg': ((0.721569, 0.721569, 0.815686), 1, u'default'), 'He': ((0.85098, 1, 1), 1, u'default'), 'Md': ((0.701961, 0.0509804, 0.65098), 1, u'default'), 'Mg': ((0.541176, 1, 0), 1, u'default'), 'dim gray': ((0.411765, 0.411765, 0.411765), 1, u'default'), 'K': ((0.560784, 0.25098, 0.831373), 1, u'default'), 'Mn': ((0.611765, 0.478431, 0.780392), 1, u'default'), 'O': ((1, 0.0509804, 0.0509804), 1, u'default'), 'dark gray': ((0.662745, 0.662745, 0.662745), 1, u'default'), 'Mt': ((0.921569, 0, 0.14902), 1, u'default'), 'S': ((1, 1, 0.188235), 1, u'default'), 'W': ((0.129412, 0.580392, 0.839216), 1, u'default'),
'Zn': ((0.490196, 0.501961, 0.690196), 1, u'default'), 'Eu': ((0.380392, 1, 0.780392), 1, u'default'), 'Zr': ((0.580392, 0.878431, 0.878431), 1, u'default'), 'Er': ((0, 0.901961, 0.458824), 1, u'default'), 'Ni': ((0.313725, 0.815686, 0.313725), 1, u'default'), 'No': ((0.741176, 0.0509804, 0.529412), 1, u'default'), 'Na': ((0.670588, 0.360784, 0.94902), 1, u'default'), 'Nb': ((0.45098, 0.760784, 0.788235), 1, u'default'), 'Nd': ((0.780392, 1, 0.780392), 1, u'default'), 'Ne': ((0.701961, 0.890196, 0.960784), 1, u'default'), 'Np': ((0, 0.501961, 1), 1, u'default'), 'Fr': ((0.258824, 0, 0.4), 1, u'default'), 'Fe': ((0.878431, 0.4, 0.2), 1, u'default'), 'Fm': ((0.701961, 0.121569, 0.729412), 1, u'default'), 'B': ((1, 0.709804, 0.709804), 1, u'default'), 'F': ((0.564706, 0.878431, 0.313725), 1, u'default'), 'Sr': ((0, 1, 0), 1, u'default'), 'N': ((0.188235, 0.313725, 0.972549), 1, u'default'), 'Kr': ((0.360784, 0.721569, 0.819608), 1, u'default'), 'Si': ((0.941176, 0.784314, 0.627451), 1, u'default'), 'Sn': ((0.4, 0.501961, 0.501961), 1, u'default'), 'Sm': ((0.560784, 1, 0.780392), 1, u'default'),
'V': ((0.65098, 0.65098, 0.670588), 1, u'default'), 'Sc': ((0.901961, 0.901961, 0.901961), 1, u'default'), 'Sb': ((0.619608, 0.388235, 0.709804), 1, u'default'), 'Sg': ((0.85098, 0, 0.270588), 1, u'default'), 'Se': ((1, 0.631373, 0), 1, u'default'), 'Co': ((0.941176, 0.564706, 0.627451), 1, u'default'), 'Cm': ((0.470588, 0.360784, 0.890196), 1, u'default'), 'Cl': ((0.121569, 0.941176, 0.121569), 1, u'default'), 'Ca': ((0.239216, 1, 0), 1, u'default'), 'Cf': ((0.631373, 0.211765, 0.831373), 1, u'default'), 'Ce': ((1, 1, 0.780392), 1, u'default'), 'Xe': ((0.258824, 0.619608, 0.690196), 1, u'default'), 'Tm': ((0, 0.831373, 0.321569), 1, u'default'), 'Cs': ((0.341176, 0.0901961, 0.560784), 1, u'default'), 'Cr': ((0.541176, 0.6, 0.780392), 1, u'default'), 'Cu': ((0.784314, 0.501961, 0.2), 1, u'default'), 'La': ((0.439216, 0.831373, 1), 1, u'default'), 'Li': ((0.8, 0.501961, 1), 1, u'default'), 'Tl': ((0.65098, 0.329412, 0.301961), 1, u'default'), 'Lu': ((0, 0.670588, 0.141176), 1, u'default'), 'Lr': ((0.780392, 0, 0.4), 1, u'default'), 'Th': ((0, 0.729412, 1), 1, u'default'),
'Ti': ((0.74902, 0.760784, 0.780392), 1, u'default'), 'Te': ((0.831373, 0.478431, 0), 1, u'default'), 'Tb': ((0.188235, 1, 0.780392), 1, u'default'), 'Tc': ((0.231373, 0.619608, 0.619608), 1, u'default'), 'Ta': ((0.301961, 0.65098, 1), 1, u'default'), 'Yb': ((0, 0.74902, 0.219608), 1, u'default'), 'Db': ((0.819608, 0, 0.309804), 1, u'default'), 'Dy': ((0.121569, 1, 0.780392), 1, u'default'), 'At': ((0.458824, 0.309804, 0.270588), 1, u'default'), 'I': ((0.580392, 0, 0.580392), 1, u'default'), 'medium purple': ((0.576471, 0.439216, 0.858824), 1, u'default'), 'U': ((0, 0.560784, 1), 1, u'default'), 'Y': ((0.580392, 1, 1), 1, u'default'), 'Ac': ((0.439216, 0.670588, 0.980392), 1, u'default'), 'Ag': ((0.752941, 0.752941, 0.752941), 1, u'default'), 'Ir': ((0.0901961, 0.329412, 0.529412), 1, u'default'), 'Am': ((0.329412, 0.360784, 0.94902), 1, u'default'), 'Al': ((0.74902, 0.65098, 0.65098), 1, u'default'), 'As': ((0.741176, 0.501961, 0.890196), 1, u'default'), 'Ar': ((0.501961, 0.819608, 0.890196), 1, u'default'), 'Au': ((1, 0.819608, 0.137255), 1, u'default'),
'Es': ((0.701961, 0.121569, 0.831373), 1, u'default'), 'In': ((0.65098, 0.458824, 0.45098), 1, u'default'), 'Mo': ((0.329412, 0.709804, 0.709804), 1, u'default'), 'light gray': ((0.827451, 0.827451, 0.827451), 1, u'default')}
	materials = {u'default': ((0.51, 0.51, 0.51), 52)}
	pbInfo = {'category': [u'distance monitor'], 'bondInfo': [{'color': (0, None, {}), 'atoms': [], 'label': (0, None, {}), 'halfbond': (0, None, {}), 'labelColor': (0, None, {}), 'labelOffset': (0, None, {}), 'drawMode': (0, None, {}), 'display': (0, None, {})}], 'lineType': (1, 2, {}), 'color': (1, 7, {}), 'optional': {'fixedLabels': (True, False, (1, False, {}))}, 'display': (1, True, {}), 'showStubBonds': (1, False, {}), 'lineWidth': (1, 1, {}), 'stickScale': (1, 1, {}), 'id': [-2]}
	modelAssociations = {}
	colorInfo = (9, (u'H', (1, 1, 1, 1)), {(u'', (1, 0, 1, 1)): [8], (u'', (0.0279974, 0.740341, 0.113875, 1)): [1], (u'O', (1, 0.0509804, 0.0509804, 1)): [4], (u'', (0.734059, 0.65845, 0.302988, 1)): [0], (u'dim gray', (0.411765, 0.411765, 0.411765, 1)): [6], (u'yellow', (1, 1, 0, 1)): [7], (u'white', (1, 1, 1, 1)): [5], (u'C', (0.564706, 0.564706, 0.564706, 1)): [2]})
	viewerInfo = {'cameraAttrs': {'center': (-1.903239470786e-16, -4.4408920985006e-16, 4.9750714326736), 'fieldOfView': 14.739475782435, 'nearFar': (11.310094000031, -5.9002567811189), 'ortho': True, 'eyeSeparation': 50.8, 'focal': -4.4735000143051}, 'viewerAttrs': {'silhouetteColor': None, 'clipping': True, 'showSilhouette': False, 'showShadows': False, 'viewSize': 11.960102564103, 'labelsOnTop': False, 'depthCueRange': (0.5, 0.9200000166893), 'silhouetteWidth': 2, 'singleLayerTransparency': True, 'shadowTextureSize': 8192, 'backgroundImage': [None, 1, 2, 1, 0, 0], 'backgroundGradient': [('Chimera default', [(1, 1, 1, 1), (0, 0, 1, 1)], 1), 1, 0, 0], 'depthCue': True, 'highlight': 0, 'scaleFactor': 1, 'angleDependentTransparency': False, 'backgroundMethod': 0}, 'viewerHL': 8, 'cameraMode': 'mono', 'detail': 15, 'viewerFog': None, 'viewerBG': 5}

	replyobj.status("Initializing session restore...", blankAfter=0,
		secondary=True)
	from SimpleSession.versions.v65 import expandSummary
	init(dict(enumerate(expandSummary(colorInfo))))
	replyobj.status("Restoring colors...", blankAfter=0,
		secondary=True)
	restoreColors(colors, materials)
	replyobj.status("Restoring molecules...", blankAfter=0,
		secondary=True)
	restoreMolecules(molInfo, resInfo, atomInfo, bondInfo, crdInfo)
	replyobj.status("Restoring surfaces...", blankAfter=0,
		secondary=True)
	restoreSurfaces(surfInfo)
	replyobj.status("Restoring VRML models...", blankAfter=0,
		secondary=True)
	restoreVRML(vrmlInfo)
	replyobj.status("Restoring pseudobond groups...", blankAfter=0,
		secondary=True)
	restorePseudoBondGroups(pbInfo)
	replyobj.status("Restoring model associations...", blankAfter=0,
		secondary=True)
	restoreModelAssociations(modelAssociations)
	replyobj.status("Restoring camera...", blankAfter=0,
		secondary=True)
	restoreViewer(viewerInfo)

try:
	restoreCoreModels()
except:
	reportRestoreError("Error restoring core models")

	replyobj.status("Restoring extension info...", blankAfter=0,
		secondary=True)


try:
	import StructMeasure
	from StructMeasure.DistMonitor import restoreDistances
	registerAfterModelsCB(restoreDistances, 1)
except:
	reportRestoreError("Error restoring distances in session")


def restoreMidasBase():
	formattedPositions = {}
	import Midas
	Midas.restoreMidasBase(formattedPositions)
try:
	restoreMidasBase()
except:
	reportRestoreError('Error restoring Midas base state')


def restoreMidasText():
	from Midas import midas_text
	midas_text.aliases = {}
	midas_text.userSurfCategories = {}

try:
	restoreMidasText()
except:
	reportRestoreError('Error restoring Midas text state')


def restore_volume_data():
 volume_data_state = \
  {
   'class': 'Volume_Manager_State',
   'data_and_regions_state': [ ],
   'version': 2,
  }
 from VolumeViewer import session
 session.restore_volume_data_state(volume_data_state)

try:
  restore_volume_data()
except:
  reportRestoreError('Error restoring volume data')


def restore_cap_attributes():
 cap_attributes = \
  {
   'cap_attributes': [
     {
      'cap_color': ( 0.4117647111415863, 0.4117647111415863, 0.4117647111415863, 1.0, ),
      'class': 'Model_Capper_State',
      'display_style': 0,
      'surface': ( 0, 0, ),
      'version': 1,
     },
    ],
   'cap_color': None,
   'cap_offset': 0.01,
   'class': 'Caps_State',
   'default_cap_offset': 0.01,
   'mesh_style': False,
   'shown': True,
   'subdivision_factor': 1.0,
   'version': 1,
  }
 import SurfaceCap.session
 SurfaceCap.session.restore_cap_attributes(cap_attributes)
registerAfterModelsCB(restore_cap_attributes)

geomData = {'AxisManager': {}, 'CentroidManager': {}, 'PlaneManager': {}}

try:
	from StructMeasure.Geometry import geomManager
	geomManager._restoreSession(geomData)
except:
	reportRestoreError("Error restoring geometry objects in session")


def restoreSession_RibbonStyleEditor():
	import SimpleSession
	import RibbonStyleEditor
	userScalings = []
	userXSections = []
	userResidueClasses = []
	residueData = [(2, 'Chimera default', 'rounded', u'unknown'), (3, 'Chimera default', 'rounded', u'unknown'), (4, 'Chimera default', 'rounded', u'unknown'), (5, 'Chimera default', 'rounded', u'unknown'), (6, 'Chimera default', 'rounded', u'unknown'), (7, 'Chimera default', 'rounded', u'unknown'), (8, 'Chimera default', 'rounded', u'unknown'), (9, 'Chimera default', 'rounded', u'unknown'), (10, 'Chimera default', 'rounded', u'unknown'), (11, 'Chimera default', 'rounded', u'unknown'), (12, 'Chimera default', 'rounded', u'unknown'), (13, 'Chimera default', 'rounded', u'unknown'), (14, 'Chimera default', 'rounded', u'unknown'), (15, 'Chimera default', 'rounded', u'unknown')]
	flags = RibbonStyleEditor.NucleicDefault1
	SimpleSession.registerAfterModelsCB(RibbonStyleEditor.restoreState,
				(userScalings, userXSections,
				userResidueClasses, residueData, flags))
try:
	restoreSession_RibbonStyleEditor()
except:
	reportRestoreError("Error restoring RibbonStyleEditor state")

trPickle = 'gAJjQW5pbWF0ZS5UcmFuc2l0aW9ucwpUcmFuc2l0aW9ucwpxASmBcQJ9cQMoVQxjdXN0b21fc2NlbmVxBGNBbmltYXRlLlRyYW5zaXRpb24KVHJhbnNpdGlvbgpxBSmBcQZ9cQcoVQZmcmFtZXNxCEsBVQ1kaXNjcmV0ZUZyYW1lcQlLAVUKcHJvcGVydGllc3EKXXELVQNhbGxxDGFVBG5hbWVxDWgEVQRtb2RlcQ5VBmxpbmVhcnEPdWJVCGtleWZyYW1lcRBoBSmBcRF9cRIoaAhLFGgJSwFoCl1xE2gMYWgNaBBoDmgPdWJVBXNjZW5lcRRoBSmBcRV9cRYoaAhLAWgJSwFoCl1xF2gMYWgNaBRoDmgPdWJ1Yi4='
scPickle = 'gAJjQW5pbWF0ZS5TY2VuZXMKU2NlbmVzCnEBKYFxAn1xA1UHbWFwX2lkc3EEfXNiLg=='
kfPickle = 'gAJjQW5pbWF0ZS5LZXlmcmFtZXMKS2V5ZnJhbWVzCnEBKYFxAn1xA1UHZW50cmllc3EEXXEFc2Iu'
def restoreAnimation():
	'A method to unpickle and restore animation objects'
	# Scenes must be unpickled after restoring transitions, because each
	# scene links to a 'scene' transition. Likewise, keyframes must be 
	# unpickled after restoring scenes, because each keyframe links to a scene.
	# The unpickle process is left to the restore* functions, it's 
	# important that it doesn't happen prior to calling those functions.
	import SimpleSession
	from Animate.Session import restoreTransitions
	from Animate.Session import restoreScenes
	from Animate.Session import restoreKeyframes
	SimpleSession.registerAfterModelsCB(restoreTransitions, trPickle)
	SimpleSession.registerAfterModelsCB(restoreScenes, scPickle)
	SimpleSession.registerAfterModelsCB(restoreKeyframes, kfPickle)
try:
	restoreAnimation()
except:
	reportRestoreError('Error in Animate.Session')

def restoreLightController():
	import Lighting
	Lighting._setFromParams({'ratio': 1.0, 'brightness': 0.9090909090909091, 'material': [52.0, (0.85, 0.85, 0.85), 0.6], 'back': [(0.35740674433659325, 0.6604015517481454, -0.6604015517481455), (1.0, 1.0, 1.0), 0.0], 'mode': 'two-point', 'key': [(0.5818540202717035, 0.6065088516391486, 0.5418421467337303), (1.0, 1.0, 1.0), 1.0], 'contrast': 0.54, 'fill': [(0.5029585598958792, 0.3205128077767858, 0.8026856340302251), (1.0, 1.0, 1.0), 0.0]})
try:
	restoreLightController()
except:
	reportRestoreError("Error restoring lighting parameters")

mdmovieData = {'length': 1, 'startFrame': None, 'endFrame': None, 'molecule': 0, 'name': 'vac.crds'}

try:
	from Movie import restoreSession
	mdmovie = restoreSession(mdmovieData)
except:
	reportRestoreError("Error restoring MD Movie interface")

mdmovieData = {'length': 1, 'startFrame': None, 'endFrame': None, 'molecule': 1, 'name': 'vac.crds'}

try:
	from Movie import restoreSession
	mdmovie = restoreSession(mdmovieData)
except:
	reportRestoreError("Error restoring MD Movie interface")


def restoreRemainder():
	from SimpleSession.versions.v65 import restoreWindowSize, \
	     restoreOpenStates, restoreSelections, restoreFontInfo, \
	     restoreOpenModelsAttrs, restoreModelClip, restoreSilhouettes

	curSelIds =  []
	savedSels = []
	openModelsAttrs = { 'cofrMethod': 4 }
	windowSize = (793, 666)
	xformMap = {0: (((-0.52041645859533, 0.67699980720708, -0.52042095525129), 111.80131286623), (-2.3007505694797, -9.9163081182259e-05, 2.5297859831222), True), 1: (((-0.91376829449117, 0.28724307500647, 0.28726106565895), 95.15769061869), (0.33650598678976, -2.0926138449201, 2.4337332158848), True)}
	fontInfo = {'face': ('Sans Serif', 'Normal', 16)}
	clipPlaneInfo = {}
	silhouettes = {0: True, 1: True, 478: True, 479: True}

	replyobj.status("Restoring window...", blankAfter=0,
		secondary=True)
	restoreWindowSize(windowSize)
	replyobj.status("Restoring open states...", blankAfter=0,
		secondary=True)
	restoreOpenStates(xformMap)
	replyobj.status("Restoring font info...", blankAfter=0,
		secondary=True)
	restoreFontInfo(fontInfo)
	replyobj.status("Restoring selections...", blankAfter=0,
		secondary=True)
	restoreSelections(curSelIds, savedSels)
	replyobj.status("Restoring openModel attributes...", blankAfter=0,
		secondary=True)
	restoreOpenModelsAttrs(openModelsAttrs)
	replyobj.status("Restoring model clipping...", blankAfter=0,
		secondary=True)
	restoreModelClip(clipPlaneInfo)
	replyobj.status("Restoring per-model silhouettes...", blankAfter=0,
		secondary=True)
	restoreSilhouettes(silhouettes)

	replyobj.status("Restoring remaining extension info...", blankAfter=0,
		secondary=True)
try:
	restoreRemainder()
except:
	reportRestoreError("Error restoring post-model state")
from SimpleSession.versions.v65 import makeAfterModelsCBs
makeAfterModelsCBs()

from SimpleSession.versions.v65 import endRestore
replyobj.status('Finishing restore...', blankAfter=0, secondary=True)
endRestore({})
replyobj.status('', secondary=True)
replyobj.status('Restore finished.')

