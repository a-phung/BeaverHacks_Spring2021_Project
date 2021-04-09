import pandas as pd
import yfinance as yf
from datetime import date, datetime, timedelta

NMS_ticker_symbols = ["AAPL", "AMZN", "GOOG", "AMAT", "AMGN", "AAL", "ADBE", "GOOGL", "ADP", "AKAM", "ATVI", "ADSK",
                      "WBA", "ARNA", "ACAD", "ALXN", "CLMS", "AVGO", "EA", "AMBA", "APOL", "LULU", "AGNC", "JBLU",
                      "ORLY", "ATML", "ACOR", "ADI", "AEGR", "ACIW", "AMTD", "ALTR", "ARCC", "AGIO", "ARLP", "AFSI",
                      "ALNY", "ARMH", "ARIA", "AINV", "ACXM", "ACHN", "ACET", "ABMD", "VA", "LIFE", "ADXS", "SAVE",
                      "AKRX", "ABAX", "ASML", "DWA", "AMCC", "CAR", "ABCO", "JKHY", "AVAV", "AMKR", "ANAC", "AEIS",
                      "MTGE", "CENX", "ASPS", "AMAG", "ALKS", "AFFX", "ACAT", "AAON", "VRSK", "ALSK", "ACTG", "ACAS",
                      "ATHN", "AVHI", "ARWR", "ANGI", "ALGN", "GLPI", "ARRS", "AMCX", "RDEN", "PAAS", "APOG", "ANDE",
                      "AMSC", "AMRS", "AMED", "ALCO", "ADUS", "ACTA", "AAWW", "MDRX", "KLIC", "AZPN", "AHGP", "SHLM",
                      "GIII", "DAVE", "AWAY", "AREX", "ANSS", "AMNB", "AIXG", "ADTN", "ACLS", "HOLI", "BEAV", "ATAX",
                      "DOX", "AVID", "ASNA", "ARAY", "AMBC", "ALGT", "AIRM", "AIMC", "ACHC", "ABY", "TA", "MANH",
                      "LAMR", "ATRO", "ATNI", "APEI", "ANIK", "ANGO", "AMSG", "ALOG", "AEGN", "ZLTQ", "WRLD", "UHAL",
                      "RJET", "CACC", "ATSG", "ASEI", "AROW", "ARCB", "AMRK", "ALRM", "AFAM", "ACSF", "ABGB", "USAP",
                      "STFC", "SEED", "BREW", "AUDC", "ATRI", "APIC", "AOSL", "AMWD", "ACGL", "ABCB", "REXI", "RAIL",
                      "ARTNA", "AGNCP", "ADRO", "KALU", "HOMB", "ATLC", "AMSWA", "AMSF", "ALLT", "AGYS", "CHOP", "CCD",
                      "AYA", "AVNW", "AMRI", "AMCN", "AGII", "AEPI", "ABCW", "SRAQU", "OMAB", "CRMT", "CRESY", "ATRA",
                      "ATEC", "ARLZ", "ARII", "ANAT", "ACRS", "ABDC", "GABC", "EPAX", "CACQ", "ASFI", "ASCMA", "ARCP",
                      "TEAM", "LMIA", "FWP", "CHY", "APLP", "AMRB", "ADAP", "ACTS", "PRTS", "BRKS", "ASYS", "AMPH",
                      "ADVS", "ABUS", "FWRD", "AGFS", "ADNC", "ACBI", "SCAI", "MTGEP", "MPAA", "AXTI", "AVXS", "ASTE",
                      "ASND", "AGIIL", "IPCC", "FNTCU", "CHI", "AGNCB", "ASMI", "ARUN", "ARCPP", "AMSGP", "AIMT",
                      "AAAP", "NBRV", "HDRAU", "AVNU", "AGFSW", "SMACU", "FSAM", "ECACR", "ARWAR", "CACGU", "AMBCW",
                      "BBRY", "BIDU", "BIIB", "BBBY", "MNST", "FITB", "BWLD", "PNRA", "CNBKA", "CBRL", "BMRN", "HBAN",
                      "PDLI", "BRCD", "BGCP", "EGLE", "PACB", "BKCC", "BBEP", "BKMU", "DNKN", "BPOP", "PBYI", "BOBE",
                      "BLUE", "NILE", "ICON", "FIBK", "EWBC", "BCRX", "BCPC", "SBGI", "BRKR", "BOKF", "VIVO", "ONB",
                      "HCBK", "COKE", "BJRI", "BCOR", "UBSH", "TCBI", "SUSQ", "SGMO", "RRGB", "LCUT", "IBTX", "FFBC",
                      "BZUN", "BGFV", "SASR", "NXST", "ZION", "VRA", "SFBS", "SBNY", "JBSS", "JACK", "BV", "BBOX",
                      "TECH", "NRIM", "NPBC", "IBKR", "BAMM", "NBIX", "FMBI", "FIVE", "CNOB", "CALA", "SBLK", "SBCF",
                      "ROLL", "HTBI", "GBDC", "FIZZ", "FFKT", "FCNCA", "BMTC", "BLKB", "BBSI", "BABY", "OZRK", "COB",
                      "CBSH", "BUSE", "BRKL", "BONT", "BOJA", "BEAT", "XBKS", "WASH", "WABC", "UCBI", "PPBI", "NBTB",
                      "MBVT", "INBK", "CSFL", "CSBK", "CATY", "BOFI", "BLMN", "BBRG", "WIFI", "WIBC", "LOB", "IBCP",
                      "FNBC", "FARM", "EBSB", "CCBG", "CBNJ", "CBF", "BIND", "BELFB", "UBNK", "TRST", "TOWN", "TBNK",
                      "SGBK", "NWBI", "NFBK", "MNRO", "LBAI", "GBT", "FBNK", "CBPO", "BSRR", "BSFT", "BPFH", "BONA",
                      "BLDR", "BIOS", "BDGE", "BDE", "BCOM", "BANF", "TRIB", "SVA", "PFBC", "IBOC", "GSBC", "STBA",
                      "SBSI", "PLAY", "OSBC", "LBRDA", "KYTH", "ISBC", "FNLC", "BSET", "BOOM", "BHBK", "BCOV", "BANR",
                      "TCBK", "SHBI", "NBBC", "MBWM", "INDB", "GBCI", "FXCB", "FBIZ", "EPAY", "TCBIP", "TBBK", "STCK",
                      "RCKY", "OKSB", "MCBC", "GBNK", "DCOM", "BUFF", "BOTA", "BBEPP", "BANX", "UBSI", "TBK", "SNBC",
                      "RBCAA", "MRLN", "HMPR", "HAWK", "FFIN", "COLB", "BRLI", "BKYF", "BBNK", "BBCN", "PWOD", "PMBC",
                      "PACW", "EVBS", "ESSA", "BPMC", "UBFO", "RVSB", "PEBO", "HWBK", "HBCP", "GNBC", "FCBC", "EBTC",
                      "BRDR", "BPOPN", "BFIN", "BECN", "WTBA", "TCBIL", "SYBT", "METR", "FSBK", "CBSHP", "BPFHW",
                      "BNCL", "BGNE", "BELFA", "SUBK", "SIBC", "LBRDK", "HBNC", "FITBI", "FBNC", "BDBD", "TCBIW",
                      "SBLKL", "GEVA", "BPOPM", "SBNYW", "OPB", "FFBCW", "CATYW", "ZIONZ", "ZIONW", "SBBP", "OSBCP",
                      "ISM", "EQBK", "CTBI", "BPFHP", "BOFIL", "BANFP", "BITI", "HBANP", "HBANO", "MSFT", "INTC",
                      "CSCO", "CMCSA", "SBUX", "COST", "CATM", "NVDA", "FTR", "CELG", "SNDK", "SCTY", "ETFC", "SYMC",
                      "DISH", "CERN", "STX", "ESRX", "CSX", "CTSH", "LRCX", "CA", "SHLD", "FAST", "WDC", "GT", "KLAC",
                      "CALM", "CTXS", "LLTC", "CME", "CHKP", "CSIQ", "GERN", "CSII", "SINA", "FOXA", "KHC", "WB",
                      "NWSA", "CHRW", "HAIN", "CTRP", "CLDX", "CINF", "CROX", "CHTR", "SWHC", "PSUN", "CREE", "TECD",
                      "SLM", "TSCO", "SPTN", "QLGC", "SPWR", "CLMT", "SANM", "CZR", "CY", "CONN", "WEN", "PSEC", "INCY",
                      "CTAS", "WBMD", "UPL", "SONC", "ROVI", "GNTX", "CRUS", "PPC", "CYOU", "CSGS", "COLM", "CEMP",
                      "XONE", "MFRM", "CYBR", "ULTA", "CPLA", "PDCO", "LNCO", "JAZZ", "CLVS", "CCIH", "CBOE", "OLED",
                      "MENT", "DEST", "CASY", "NUAN", "MTSC", "MSCC", "MPEL", "FSC", "ERIE", "CLNE", "UTHR", "ISIL",
                      "INFN", "CPLP", "ZBRA", "UTSI", "SIMO", "SBAC", "NEOG", "NAVI", "LKQ", "LANC", "FDML", "CDW",
                      "SCVL", "RPTP", "PCH", "NTRS", "MASI", "LMCA", "JASO", "ISLE", "CSGP", "CG", "CAKE", "SNC",
                      "SCHL", "PRTA", "PRGS", "ORIT", "NWS", "MIK", "LSCC", "IRBT", "FOX", "DISCA", "CAMP", "XCRA",
                      "SBRA", "PRXL", "PRSC", "OTEX", "NCLH", "HFWA", "HBHC", "FLDM", "EMMS", "CRAY", "COHU", "UMPQ",
                      "RPXC", "NDSN", "GEOS", "ELNK", "ECPG", "DGAS", "CYNO", "CAFD", "CAC", "VICR", "SIAL", "SATS",
                      "RSYS", "RECN", "POOL", "MEOH", "LOPE", "LINC", "IBKC", "GPOR", "FSTR", "DMRC", "CSCD", "CMCSK",
                      "CDK", "CASH", "VOXX", "TAXI", "PNNT", "ON", "MDCO", "MANT", "LMNX", "IXYS", "HRZN", "HMSY",
                      "FNSR", "DISCK", "CTRN", "CSAL", "CRZO", "CRTO", "CPHD", "COWN", "COMM", "CCNE", "CAVM", "TRMK",
                      "TESO", "SMCI", "ROIC", "PRIM", "PODD", "NATI", "LMCK", "ISCA", "INAP", "HWCC", "FTD", "FMER",
                      "FBRC", "CYTK", "CWCO", "CVGW", "CTRE", "CSOD", "CORE", "CMCO", "CFMS", "CDNS", "SPNC", "SGI",
                      "PLCE", "PCTY", "PCCC", "NDLS", "KEYW", "IPGP", "HOFT", "HAFC", "GNCMA", "EFSC", "CVLT", "CVBF",
                      "CNSL", "CHKE", "CETV", "CECO", "CCRN", "CASS", "VWR", "UCTT", "TRS", "THOR", "THFF", "TFSL",
                      "STRL", "SNHY", "PRSS", "NWPX", "MATW", "LDRH", "IRDM", "IMMR", "GLRE", "FELE", "FDUS", "ELRC",
                      "CPRT", "CMTL", "CCXI", "CCOI", "WDFC", "TW", "TICC", "SP", "SHEN", "SGMS", "RNST", "OTTR",
                      "MTRX", "IMOS", "ICLR", "HMHC", "GOOD", "FULT", "FRME", "FEIC", "CVGI", "CSTE", "CNMD", "CISG",
                      "CHEF", "CHDN", "CHCO", "CGNX", "VSEC", "UMBF", "SPIL", "SCSS", "QUMU", "QDEL", "PWRD", "NTLS",
                      "NCMI", "HTHT", "DCIX", "CWST", "CVTI", "CTWS", "CTCM", "CRAI", "CHMA", "CGO", "TCRD", "TCPC",
                      "SRCE", "SABR", "PMTS", "PLXS", "PLPC", "PGC", "OPHT", "OCFC", "NMRX", "MBTF", "LNDC", "LKFN",
                      "KOPN", "IART", "FRAN", "DTLK", "CRNT", "COHR", "CNTF", "CMPR", "CFFN", "ZIXI", "YORW", "VRTU",
                      "SMTC", "SLRC", "RGEN", "MIDD", "HURC", "GAIN", "CYBX", "CTRL", "CRWN", "CPSI", "CKEC", "CHMG",
                      "CHFC", "WSTC", "WSFS", "WIRE", "UCFC", "SPSC", "PBPB", "NRCIB", "MSEX", "MCRI", "LORL", "LION",
                      "LAYN", "KZ", "HQCL", "GLAD", "FSRV", "ELON", "CXRX", "CUTR", "CONE", "COBZ", "CHUY", "CECE",
                      "CDXS", "TUES", "SFNC", "SEIC", "RENT", "PSTB", "PFMT", "HTBK", "FSFR", "FOGO", "FDEF", "CTG",
                      "CRVL", "CPTA", "COLL", "CHSCP", "CEVA", "CENT", "CCMP", "UVSP", "TAST", "SUNS", "SSB", "PSEM",
                      "PKOH", "PFIS", "PCBK", "NATL", "LMOS", "KRNY", "ITRN", "INFA", "IGTE", "GLDD", "GARS", "FFIC",
                      "DWSN", "CVCO", "CSWC", "CPIX", "CFNL", "CFFI", "STLY", "SBRAP", "PULB", "PFLT", "OXLC", "OFS",
                      "NRCIA", "NEWP", "MCGC", "JRJC", "JJSF", "HCCI", "GAINO", "FUNC", "FSV", "FOXF", "CTHR", "CSUN",
                      "CSQ", "CRRC", "CPHR", "COVS", "CMFN", "CKSW", "CENTA", "WTFC", "WLTW", "TGA", "SENEB", "SENEA",
                      "NCOM", "MRD", "MRCC", "LOJN", "LMNR", "LABL", "ITIC", "IRCP", "GTLS", "DLTR", "XRAY", "ODP",
                      "DXCM", "DATE", "DMND", "ODFL", "IDTI", "DAKT", "KTOS", "FANG", "DMLP", "DEPO", "DTSI", "STLD",
                      "DGII", "DGICA", "SIRO", "SIGM", "DORM", "DXPE", "KRNT", "DIOD", "DFRG", "DRNA", "DERM", "TWIN",
                      "TRAK", "DXM", "DSPG", "DSGX", "DXLG", "DLTH", "QQQX", "DSKY", "DMTX", "DHIL", "VDTH", "UDF",
                      "MDM", "DISCB", "DBVT", "DHXM", "DGICB", "CHW", "YERR", "EBAY", "LINE", "EXPE", "EXPD", "EXEL",
                      "ENDP", "EQIX", "EGHT", "EXXI", "MCEP", "UEIC", "MGEE", "IEP", "ERIC", "ECHO", "EVEP", "PNK",
                      "STRA", "ERII", "ECYT", "ENSG", "ELGX", "ENOC", "EBIX", "LOCO", "EXTR", "EXPO", "ESGR", "EFII",
                      "REGI", "EIGI", "ECOL", "PTEN", "PETS", "EVLV", "ENTA", "PEGI", "LECO", "FNGN", "EZPW", "EXLS",
                      "ESLT", "EPIQ", "EGOV", "PERY", "PDCE", "EXFO", "WERN", "EXAC", "EROC", "EMITF", "EEFT", "SPKE",
                      "PLUS", "NSIT", "MFLX", "EHTH", "VNOM", "ELOS", "MGIC", "LONG", "ETSY", "ENTG", "EMCI", "SYKE",
                      "RELL", "HEES", "FXEN", "EXLP", "ESND", "EPZM", "ENVI", "RUSHA", "EZCH", "ESIO", "EDIT", "SFXE",
                      "HTLD", "EDGE", "SPI", "EMMSP", "RUSHB", "KE", "ENZY", "FXENP", "EBAYL", "FB", "FSLR", "WFM",
                      "FFIV", "FISV", "FLEX", "FEYE", "FTNT", "FLIR", "FLWS", "PBCT", "FOSL", "UFCS", "SIVB", "SFM",
                      "UFPI", "UNFI", "FCS", "FARO", "TFM", "SVVC", "FNFG", "LPLA", "FUEL", "KCAP", "GIFI", "FRGI",
                      "FMI", "FISI", "MBFI", "FORM", "FINL", "FFNW", "WSBF", "SAFM", "MSFG", "GSM", "FSYS", "FRED",
                      "FORR", "WFD", "VIRT", "NEWS", "NATH", "INTL", "FPRX", "NICK", "MOFG", "FRSH", "WAFD", "SNAK",
                      "PROV", "LTXB", "HTLF", "FTEK", "FORTY", "FRPH", "FGEN", "PNFP", "FLXS", "SIVBO", "HBOS", "FUND",
                      "FISH", "WHF", "MNRK", "FSCFL", "SQBK", "INTLL", "WTFCM", "WHFBL", "WAFDW", "FTRPR", "WSFSL",
                      "WTFCW", "GILD", "MRVL", "VOD", "PCLN", "GMCR", "GRPN", "GPRO", "GRMN", "TROW", "Z", "KNDI",
                      "RGLD", "GPRE", "GLBL", "MLNK", "GOV", "GOLD", "JCOM", "HCSG", "GLUU", "MYGN", "LBTYA", "ULTI",
                      "GOGO", "HSON", "SGEN", "ININ", "GLNG", "GILT", "THRM", "GSOL", "GAME", "WMGI", "PENN", "SIGI",
                      "RUTH", "QVCA", "LBTYK", "IILG", "VNET", "NAVG", "PRAA", "KTWO", "IRG", "HMIN", "GMLP", "GMAN",
                      "GHDX", "ROCK", "PRGX", "MOLG", "LILA", "HUBG", "GSIT", "GSIG", "NWLI", "KANG", "HCKT", "GRFS",
                      "WEB", "NAME", "MYRG", "MTCH", "LHCG", "GK", "GBLI", "WEYS", "GOGL", "IGLD", "GURE", "GASS",
                      "CIGI", "TRNX", "SAFT", "LILAK", "GOODN", "GLPG", "HURN", "ZG", "WWWW", "SUTR", "LBTYB", "JRVR",
                      "GAINN", "QVCB", "GRSHU", "GAINP", "GLADO", "GOODP", "GBLIZ", "OPK", "SIRI", "HAS", "PYPL",
                      "MHLD", "HSIC", "HA", "HZNP", "WIN", "HIMX", "SNH", "HOLX", "HPT", "NIHD", "HWKN", "HDS", "SSNC",
                      "RYAAY", "HSNI", "HSII", "MLHR", "PICO", "HTCH", "HSTM", "HIBB", "TYPE", "MKTX", "JBHT", "SLGN",
                      "INOV", "HLIT", "TTS", "MTSI", "LGIH", "IPCM", "HWAY", "HMST", "IPHS", "HTWR", "HELE", "HDP",
                      "MGLN", "HALO", "TTEC", "SPOK", "LPNT", "INCR", "HCOM", "HAYN", "SPWH", "LITE", "HQY", "TSC",
                      "PRAH", "LTRPA", "ZINC", "WLRHU", "SHLDW", "HCM", "HKTV", "HDNG", "HBHCL", "LTRPB", "SPNE",
                      "PATI", "MHLDO", "TSLA", "YHOO", "NFLX", "QCOM", "MU", "REGN", "TXN", "MAT", "SPLS", "INO", "MAR",
                      "VRTX", "ZNGA", "RLYP", "ROST", "MDLZ", "TMUS", "SWKS", "ISRG", "SRCL", "PAYX", "MCHP", "XLNX",
                      "MXIM", "URBN", "NTAP", "INTU", "ILMN", "PCAR", "SRPT", "MDVN", "ICPT", "SOHU", "NTES", "TERP",
                      "TASR", "YY", "VRSN", "VVUS", "SWIR", "JD", "NDAQ", "NVAX", "VIAB", "MDSO", "TRIP", "WPRT", "VIA",
                      "RMBS", "RCII", "PMCS", "NYMT", "JUNO", "PTCT", "SYNA", "IDXX", "PTLA", "PCRX", "ONTY", "TIVO",
                      "SNPS", "SPPI", "QSII", "UNTD", "PZZA", "STMP", "RARE", "SNI", "IDCC", "SPLK", "SIR", "QRVO",
                      "OCLR", "ZUMZ", "YRCW", "WWD", "VRNT", "SAAS", "ORIG", "MMSI", "INFI", "IMGN", "ZU", "TTWO",
                      "TTEK", "SZYM", "QLIK", "PLCM", "OUTR", "MELI", "LSTR", "UBNT", "TUBE", "SKYW", "SKUL", "SIEN",
                      "RAVN", "ONCE", "NTGR", "LLNW", "WRES", "SQNM", "SONS", "SNCR", "SGYP", "SFLY", "MGPI", "MCRB",
                      "JAKK", "ITRI", "IIIN", "ZEUS", "TXRH", "TTPH", "KITE", "XNPT", "TILE", "SODA", "SHLO", "REIS",
                      "PLAB", "OREX", "ORBC", "NTCT", "MSTR", "MPWR", "JOBS", "IQNT", "IPXL", "ZFGN", "WSBC", "TSYS",
                      "TSRA", "TREE", "TNGO", "SPAR", "RTIX", "PTC", "PRFT", "OMCL", "OIIM", "NXTM", "NUVA", "NTK",
                      "LYTS", "LXRX", "LPSN", "IRWD", "WOOF", "TZOO", "SEAC", "SCLN", "SCHN", "RP", "PGNX", "OSIS",
                      "MTEX", "JOUT", "XBIT", "WING", "SZMK", "SEDG", "QNST", "PSMT", "MIND", "MGI", "LOGM", "LNCE",
                      "KELYA", "INSM", "ZAGG", "XXIA", "VTAE", "VSAR", "VRTS", "TAX", "SAIA", "RSTI", "QLYS", "PTIE",
                      "PLKI", "OVTI", "MXWL", "MRCY", "MORN", "MNTA", "MIFI", "MERC", "KVHI", "IONS", "IMPV", "IMKTA",
                      "ICFI", "VSAT", "UPIP", "TNAV", "SYNT", "STRS", "SREV", "SRDX", "POZN", "NK", "MTSN", "MLAB",
                      "MKTO", "MINI", "IIVI", "UEPS", "TRUE", "TRGT", "THRX", "TEDU", "STKL", "SHOR", "RIGL", "QLTI",
                      "POWL", "PDFS", "NTRI", "NANO", "KPTI", "ITCI", "ICUI", "VIAV", "VASC", "JIVE", "JST", "IIJI",
                      "JSM", "JNP", "KMDA", "KIRK", "KFX", "KBAL", "KFRC", "KURA", "KLXI", "KELYB", "WYNN", "VNR",
                      "VIP", "SSYS", "MLNX", "MEMP", "LGCY", "RDWR", "WIX", "NCTY", "TSEM", "SHOO", "MMLP", "PERI",
                      "NICE", "TRMB", "SILC", "NVCR", "MRTN", "ORBK", "MCOX", "LVNTA", "LOGI", "LIOX", "LAWS", "SLAB",
                      "LFUS", "VNRBP", "VNRAP", "MMYT", "XNET", "LMNS", "SEMI", "MOBI", "LQDT", "PTXP", "PTNR", "OXLCO",
                      "CCLP", "USLM", "STNR", "RRM", "MRKT", "LVNTB", "VNRCP", "NVMI", "MIME", "MESO", "LIVN", "LGCYO",
                      "OXLCP", "OXLCN", "LGCYP", "MYL", "TITN", "UTMD", "WMAR", "VISN", "MOMO", "MGRC", "MGNX", "MDCA",
                      "MARPS", "MYOK", "MTLS", "MKSI", "SMRT", "MOBL", "MDAS", "MCRL", "MCHX", "MITL", "VLGEA", "NYMTO",
                      "SKLNU", "INFO", "NYMTP", "NXPI", "QGEN", "NKTR", "YNDX", "QURE", "OFIX", "NSSC", "NNBR", "NTRA",
                      "PKT", "NCIT", "CNV", "NUTR", "NTRSP", "OSUR", "OMED", "OTIC", "OCLSW", "OHAI", "ONNN", "WPPGY",
                      "SHPG", "QIWI", "PCYC", "SGNT", "POWI", "PEGA", "ISIS", "IPAR", "PATK", "PHII", "SNDX", "PHIIK",
                      "PVTB", "PINC", "PCTI", "SGRY", "CSRE", "TECU", "PMFG", "PVTBP", "CLTX", "QADA", "QADB", "SALE",
                      "SSRI", "RUN", "RNWK", "RLOC", "RNET", "RCPT", "RELY", "RGNX", "REMY", "STRZA", "SCSC", "USTR",
                      "SYUT", "SQI", "STB", "ISSC", "ISSI", "VRNS", "UACL", "SLMAP", "SLMBP", "STRZB", "SRCLP", "SRSC",
                      "TWOU", "TLGT", "TSRO", "VYGR", "VTL", "USAK", "TRVN", "TRIV", "TTMI", "TESS", "CTMX", "UTEK",
                      "UTIW", "UBIC", "INVA", "TMUSP", "VECO", "VIAVV", "WETF", "WILN", "WINVV", "XOOM", "YDLE",
                      "ZCVVV", "ZAVVV", "APSA", "ASPX", "FNBG", "BSDM", "CTRX", "CBRX", "CERCZ", "CFRXW", "CHSCM",
                      "CHSCN", "CHSCL", "CHSCO", "CHYR", "CMSB", "CTCT", "IBKCP", "CSWI", "CSALV", "CSWIV", "DRIV",
                      "EDS", "EOPN", "ESBF", "EVRY", "FCZA", "FCZAP", "MBFIP", "MFIN", "GOODO", "COWNL", "HBNK", "HLSS",
                      "HPTX", "HTWO", "IAC", "IARTV", "IBCA", "ICEL", "IMI", "IMRS", "IOSP", "IPAS", "IRDMB", "IVAC",
                      "IVAN", "KURO", "LEVYU", "LEVY", "LPHI", "MWIV", "NBTF", "NOVB", "NPSP", "PEOP", "PETM", "PENX",
                      "PRLS", "PTRY", "RGDO", "RNA", "RRST", "RVBD", "SGRH", "SIMG", "SLXP", "TGE", "UPI", "VIEW",
                      "VLCCF", "VOLC", "VSCI", "VTSS", "WLBPZ", "CHEKU", "CNDO", "COBK", "INGN", "INWK", "LILKV",
                      "LILAV", "LITEV", "SPNEV"]

# Get user input: one stock ticker and a time horizon of a min of one day and max of six months.
ticker = input("Please enter a stock symbol or ticker: ").upper()

while ticker not in NMS_ticker_symbols:
    ticker = input("Please reenter a valid stock symbol or ticker: ").upper()

future_date = input("Please enter a future time up to six months from the present in the format "
                    "'YYYY-MM-DD' to predict the price on that date: ")

while True:
    def date_check(user_date):
        """Verifies that the date inputted by user is in the correct format, and is greater than
        the present date and less than six months in the future.
        """
        today = date.today()
        six_months = today + timedelta(days=180)
        if len(str(today)) != len(user_date):
            return False
        if user_date[4] != "-" or user_date[7] != "-":
            return False

        future_year = int(user_date[:4])
        future_month = int(user_date[5:7])
        future_day = int(user_date[8:])

        past_date = today > datetime(future_year, future_month, future_day).date()
        past_max = six_months < datetime(future_year, future_month, future_day).date()

        if past_date or past_max:
            return False
        else:
            return True

    result = date_check(future_date)
    if result:
        break
    else:
        future_date = input("Please reenter a valid future date up to six months from the present "
                            "in the format 'YYYY-MM-DD' to predict the price on that date: ")


