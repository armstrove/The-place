ralias plus minus M1_lvsres w=w l=l rval=0.001
.ends

ralias plus minus M2_lvsres w=w l=l rval=0.001
.ends

ralias plus minus M3_lvsres w=w l=l rval=0.001
.ends

ralias plus minus M4_lvsres w=w l=l rval=0.001
.ends

ralias plus minus D5_lvsres w=w l=l rval=0.001
.ends

ralias plus minus D6_lvsres w=w l=l rval=0.001
.ends

ralias plus minus D7_lvsres w=w l=l rval=0.001
.ends

ralias plus minus D8_lvsres w=w l=l rval=0.001
.ends

ralias plus minus D9_lvsres w=w l=l rval=0.001
.ends

ralias plus minus D10_lvsres w=w l=l rval=0.001
.ends

ralias plus minus D11_lvsres w=w l=l rval=0.001
.ends

ralias plus minus IA_lvsres w=w l=l rval=0.001
.ends

ralias plus minus IB_lvsres w=w l=l rval=0.001
.ends

ralias plus minus IA_lvsres w=w l=l rval=0.001
.ends

ralias plus minus IB_lvsres w=w l=l rval=0.001
.ends

ralias plus minus LB_lvsres l=l w=w rval=0.001
.ends

ralias plus minus LB_lvsres l=l w=w rval=0.001
.ends

.SUBCKT vncap_2t A B
.ENDS

*.PININFO a:I drv_en:I drv_en_n:I gd:I n:O p:O vreg_tx_drv:I
MPp p a qq vreg_tx_drv slvtpfet l=8n nf=1 nfin=4 fpitch=0.027u m=2 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
MPn n a pp vreg_tx_drv slvtpfet l=8n nf=1 nfin=4 fpitch=0.027u m=2 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
MPswp qq drv_en_n vreg_tx_drv vreg_tx_drv lvtpfet l=8n nf=1 nfin=4 fpitch=0.027u m=4 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
MP_dmy vreg_tx_drv vreg_tx_drv vreg_tx_drv vreg_tx_drv lvtpfet l=8n nf=1 nfin=4 fpitch=0.027u m=4 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
MP_dmy_2 vreg_tx_drv vreg_tx_drv vreg_tx_drv vreg_tx_drv lvtpfet l=8n nf=1 nfin=4 fpitch=0.027u m=3 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
MP_dmy_3 vreg_tx_drv vreg_tx_drv vreg_tx_drv vreg_tx_drv lvtpfet l=8n nf=1 nfin=4 fpitch=0.027u m=8 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
MPswn pp drv_en_n vreg_tx_drv vreg_tx_drv lvtpfet l=8n nf=1 nfin=4 fpitch=0.027u m=4 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
MPpdp p drv_en vreg_tx_drv vreg_tx_drv lvtpfet l=8n nf=1 nfin=4 fpitch=0.027u m=1 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
MNp p a oo gd slvtnfet l=8n nf=1 nfin=4 fpitch=0.027u m=2 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
MNn n a nn gd slvtnfet l=8n nf=1 nfin=4 fpitch=0.027u m=2 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
MN_dmy gd gd gd gd lvtnfet l=8n nf=1 nfin=4 fpitch=0.027u m=4 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
MN_dmy_2 gd gd gd gd lvtnfet l=8n nf=1 nfin=4 fpitch=0.027u m=3 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
MNpdn n drv_en_n gd gd lvtnfet l=8n nf=1 nfin=4 fpitch=0.027u m=1 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
MN_dmy_3 gd gd gd gd lvtnfet l=8n nf=1 nfin=4 fpitch=0.027u m=8 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
MNswp oo drv_en gd gd lvtnfet l=8n nf=1 nfin=4 fpitch=0.027u m=4 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
MNswn nn drv_en gd gd lvtnfet l=8n nf=1 nfin=4 fpitch=0.027u m=4 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
*.PININFO boostn:I bpass:B drv_en:I gd:B ndrv:I nout:B
Mn_sw2 n_mid boostn bpass gd lvtnfet l=8n nf=1 nfin=8 fpitch=0.027u m=8 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
Mn_sw1 nout drv_en n_mid gd lvtnfet l=8n nf=1 nfin=8 fpitch=0.027u m=8 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
Mn_sw_dm_ gd gd gd gd lvtnfet l=8n nf=1 nfin=8 fpitch=0.027u m=6 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
Mn_sw n_mid ndrv gd gd lvtnfet l=8n nf=1 nfin=8 fpitch=0.027u m=6 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
*.PININFO gd:B mid_dn:B mid_up:B pre_r:B vout:B
rRfix_par2 pre_r mid_dn rmres w=1.32u l=1.7u r=673.962 rmdir=2 drawfill=0 m=1 pbar=1 sbar=1 orientation=2 r_cut=0 ncr=2 $SUB=gd
rRfix_par4 mid_dn vout rmres w=1.32u l=1.7u r=673.962 rmdir=2 drawfill=0 m=1 pbar=1 sbar=1 orientation=2 r_cut=0 ncr=2 $SUB=gd
rRfix_par1 mid_up vout rmres w=1.32u l=1.7u r=673.962 rmdir=2 drawfill=0 m=1 pbar=1 sbar=1 orientation=2 r_cut=0 ncr=2 $SUB=gd
rRfix_par0 pre_r mid_up rmres w=1.32u l=1.7u r=673.962 rmdir=2 drawfill=0 m=1 pbar=1 sbar=1 orientation=2 r_cut=0 ncr=2 $SUB=gd
*.PININFO boostp:I bpass:B drv_en_n:I pdrv:I pout:B vreg_tx_drv:B
Mp_sw1 pout drv_en_n p_mid vreg_tx_drv lvtpfet l=8n nf=1 nfin=8 fpitch=0.027u m=12 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
Mp_sw p_mid pdrv vreg_tx_drv vreg_tx_drv lvtpfet l=8n nf=1 nfin=8 fpitch=0.027u m=6 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
Mp_sw2 bpass boostp p_mid vreg_tx_drv lvtpfet l=8n nf=1 nfin=8 fpitch=0.027u m=8 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
*.PININFO boostn:I boostp:I data_serial:I drv_en:I drv_en_n:I gd:B vout:B vreg_tx_drv:B
Xdrv data_serial drv_en drv_en_n gd ndrv pdrv vreg_tx_drv tx_vdriver_mos_drv
Xpdn boostn bpass_dn drv_en gd ndrv pre_r tx_vdriver_down_full_boost
Xres_full gd bpass_dn bpass_up pre_r vout tx_vdriver_res_full_boost
xI79 pre_r vflag v=0.75
xI77 vout vflag v=0.75
xI76 pre_r vflag v=0.75
Xpup boostp bpass_up drv_en_n pdrv pre_r vreg_tx_drv tx_vdriver_up_full_boost
*.PININFO a:I gd:B vp:B z:O
MM0 z a gd gd lvtnfet l=8n nf=1 nfin=8 fpitch=0.027u m=4 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
MM1 z a vp vp lvtpfet l=8n nf=1 nfin=8 fpitch=0.027u m=4 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
*.PININFO gd:B vp:B
MN1 gd gd gd gd lvtnfet l=8n nf=1 nfin=4 fpitch=0.027u m=4 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
MP2 vp vp vp vp lvtpfet l=8n nf=1 nfin=4 fpitch=0.027u m=4 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
*.PININFO gd:B vp:B
MP4 net10 net10 net10 vp lvtpfet l=8n nf=1 nfin=5 fpitch=0.027u m=2 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
MP0 vp net11 vp vp lvtpfet l=8n nf=1 nfin=5 fpitch=0.027u m=4 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
MM1 net10 net11 vp vp lvtpfet l=8n nf=1 nfin=5 fpitch=0.027u m=1 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
MN1 gd net10 net11 gd lvtnfet l=8n nf=1 nfin=5 fpitch=0.027u m=1 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
MN5 net11 net11 net11 gd lvtnfet l=8n nf=1 nfin=5 fpitch=0.027u m=2 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
MM0 gd net10 gd gd lvtnfet l=8n nf=1 nfin=5 fpitch=0.027u m=4 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
*.PININFO boostn:I boostp:I data_ser_m:I data_ser_p:I drv_en:I drv_en_n:I gd:B tx_m:B tx_p:B vreg_tx_drv:B
Xdrv_p boostn_bar boostp_bar data_ser_p drv_en drv_en_n gd tx_p vreg_tx_drv tx_vdriver_mos_full
Xdrv_m boostn_bar boostp_bar data_ser_m drv_en drv_en_n gd tx_m vreg_tx_drv tx_vdriver_mos_full
Xinv_boostp boostp gd vreg_tx_drv boostp_bar custom_inv64x
Xinv_boostn boostn gd vreg_tx_drv boostn_bar custom_inv64x
XI69 gd vreg_tx_drv sc_lvt_fill_6poly
XI68<0> gd vreg_tx_drv sc_lvt_decap_nf_4
XI68<1> gd vreg_tx_drv sc_lvt_decap_nf_4
ralias plus minus M1_lvsres w=w l=l rval=0.001
.ends

ralias plus minus M2_lvsres w=w l=l rval=0.001
.ends

ralias plus minus M3_lvsres w=w l=l rval=0.001
.ends

ralias plus minus M4_lvsres w=w l=l rval=0.001
.ends

ralias plus minus D5_lvsres w=w l=l rval=0.001
.ends

ralias plus minus D6_lvsres w=w l=l rval=0.001
.ends

ralias plus minus D7_lvsres w=w l=l rval=0.001
.ends

ralias plus minus D8_lvsres w=w l=l rval=0.001
.ends

ralias plus minus D9_lvsres w=w l=l rval=0.001
.ends

ralias plus minus D10_lvsres w=w l=l rval=0.001
.ends

ralias plus minus D11_lvsres w=w l=l rval=0.001
.ends

ralias plus minus IA_lvsres w=w l=l rval=0.001
.ends

ralias plus minus IB_lvsres w=w l=l rval=0.001
.ends

ralias plus minus IA_lvsres w=w l=l rval=0.001
.ends

ralias plus minus IB_lvsres w=w l=l rval=0.001
.ends

ralias plus minus LB_lvsres l=l w=w rval=0.001
.ends

ralias plus minus LB_lvsres l=l w=w rval=0.001
.ends

.SUBCKT vncap_2t A B
.ENDS

*.PININFO a:I drv_en:I drv_en_n:I gd:I n:O p:O vreg_tx_drv:I
MPp p a qq vreg_tx_drv slvtpfet l=8n nf=1 nfin=4 fpitch=0.027u m=2 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
MPn n a pp vreg_tx_drv slvtpfet l=8n nf=1 nfin=4 fpitch=0.027u m=2 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
MPswp qq drv_en_n vreg_tx_drv vreg_tx_drv lvtpfet l=8n nf=1 nfin=4 fpitch=0.027u m=4 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
MP_dmy vreg_tx_drv vreg_tx_drv vreg_tx_drv vreg_tx_drv lvtpfet l=8n nf=1 nfin=4 fpitch=0.027u m=4 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
MP_dmy_2 vreg_tx_drv vreg_tx_drv vreg_tx_drv vreg_tx_drv lvtpfet l=8n nf=1 nfin=4 fpitch=0.027u m=3 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
MP_dmy_3 vreg_tx_drv vreg_tx_drv vreg_tx_drv vreg_tx_drv lvtpfet l=8n nf=1 nfin=4 fpitch=0.027u m=8 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
MPswn pp drv_en_n vreg_tx_drv vreg_tx_drv lvtpfet l=8n nf=1 nfin=4 fpitch=0.027u m=4 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
MPpdp p drv_en vreg_tx_drv vreg_tx_drv lvtpfet l=8n nf=1 nfin=4 fpitch=0.027u m=1 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
MNp p a oo gd slvtnfet l=8n nf=1 nfin=4 fpitch=0.027u m=2 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
MNn n a nn gd slvtnfet l=8n nf=1 nfin=4 fpitch=0.027u m=2 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
MN_dmy gd gd gd gd lvtnfet l=8n nf=1 nfin=4 fpitch=0.027u m=4 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
MN_dmy_2 gd gd gd gd lvtnfet l=8n nf=1 nfin=4 fpitch=0.027u m=3 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
MNpdn n drv_en_n gd gd lvtnfet l=8n nf=1 nfin=4 fpitch=0.027u m=1 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
MN_dmy_3 gd gd gd gd lvtnfet l=8n nf=1 nfin=4 fpitch=0.027u m=8 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
MNswp oo drv_en gd gd lvtnfet l=8n nf=1 nfin=4 fpitch=0.027u m=4 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
MNswn nn drv_en gd gd lvtnfet l=8n nf=1 nfin=4 fpitch=0.027u m=4 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
*.PININFO boostn:I bpass:B drv_en:I gd:B ndrv:I nout:B
Mn_sw2 n_mid boostn bpass gd lvtnfet l=8n nf=1 nfin=8 fpitch=0.027u m=8 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
Mn_sw1 nout drv_en n_mid gd lvtnfet l=8n nf=1 nfin=8 fpitch=0.027u m=8 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
Mn_sw_dm_ gd gd gd gd lvtnfet l=8n nf=1 nfin=8 fpitch=0.027u m=6 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
Mn_sw n_mid ndrv gd gd lvtnfet l=8n nf=1 nfin=8 fpitch=0.027u m=6 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
*.PININFO gd:B mid_dn:B mid_up:B pre_r:B vout:B
rRfix_par2 pre_r mid_dn rmres w=1.32u l=1.7u r=673.962 rmdir=2 drawfill=0 m=1 pbar=1 sbar=1 orientation=2 r_cut=0 ncr=2 $SUB=gd
rRfix_par4 mid_dn vout rmres w=1.32u l=1.7u r=673.962 rmdir=2 drawfill=0 m=1 pbar=1 sbar=1 orientation=2 r_cut=0 ncr=2 $SUB=gd
rRfix_par1 mid_up vout rmres w=1.32u l=1.7u r=673.962 rmdir=2 drawfill=0 m=1 pbar=1 sbar=1 orientation=2 r_cut=0 ncr=2 $SUB=gd
rRfix_par0 pre_r mid_up rmres w=1.32u l=1.7u r=673.962 rmdir=2 drawfill=0 m=1 pbar=1 sbar=1 orientation=2 r_cut=0 ncr=2 $SUB=gd
*.PININFO boostp:I bpass:B drv_en_n:I pdrv:I pout:B vreg_tx_drv:B
Mp_sw1 pout drv_en_n p_mid vreg_tx_drv lvtpfet l=8n nf=1 nfin=8 fpitch=0.027u m=12 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
Mp_sw p_mid pdrv vreg_tx_drv vreg_tx_drv lvtpfet l=8n nf=1 nfin=8 fpitch=0.027u m=6 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
Mp_sw2 bpass boostp p_mid vreg_tx_drv lvtpfet l=8n nf=1 nfin=8 fpitch=0.027u m=8 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
*.PININFO boostn:I boostp:I data_serial:I drv_en:I drv_en_n:I gd:B vout:B vreg_tx_drv:B
Xdrv data_serial drv_en drv_en_n gd ndrv pdrv vreg_tx_drv tx_vdriver_mos_drv
Xpdn boostn bpass_dn drv_en gd ndrv pre_r tx_vdriver_down_full_boost
Xres_full gd bpass_dn bpass_up pre_r vout tx_vdriver_res_full_boost
xI79 pre_r vflag v=0.75
xI77 vout vflag v=0.75
xI76 pre_r vflag v=0.75
Xpup boostp bpass_up drv_en_n pdrv pre_r vreg_tx_drv tx_vdriver_up_full_boost
*.PININFO a:I gd:B vp:B z:O
MM0 z a gd gd lvtnfet l=8n nf=1 nfin=8 fpitch=0.027u m=4 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
MM1 z a vp vp lvtpfet l=8n nf=1 nfin=8 fpitch=0.027u m=4 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
*.PININFO gd:B vp:B
MN1 gd gd gd gd lvtnfet l=8n nf=1 nfin=4 fpitch=0.027u m=4 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
MP2 vp vp vp vp lvtpfet l=8n nf=1 nfin=4 fpitch=0.027u m=4 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
*.PININFO gd:B vp:B
MP4 net10 net10 net10 vp lvtpfet l=8n nf=1 nfin=5 fpitch=0.027u m=2 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
MP0 vp net11 vp vp lvtpfet l=8n nf=1 nfin=5 fpitch=0.027u m=4 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
MM1 net10 net11 vp vp lvtpfet l=8n nf=1 nfin=5 fpitch=0.027u m=1 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
MN1 gd net10 net11 gd lvtnfet l=8n nf=1 nfin=5 fpitch=0.027u m=1 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
MN5 net11 net11 net11 gd lvtnfet l=8n nf=1 nfin=5 fpitch=0.027u m=2 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
MM0 gd net10 gd gd lvtnfet l=8n nf=1 nfin=5 fpitch=0.027u m=4 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
*.PININFO boostn:I boostp:I data_ser_m:I data_ser_p:I drv_en:I drv_en_n:I gd:B tx_m:B tx_p:B vreg_tx_drv:B
Xdrv_p boostn_bar boostp_bar data_ser_p drv_en drv_en_n gd tx_p vreg_tx_drv tx_vdriver_mos_full
Xdrv_m boostn_bar boostp_bar data_ser_m drv_en drv_en_n gd tx_m vreg_tx_drv tx_vdriver_mos_full
Xinv_boostp boostp gd vreg_tx_drv boostp_bar custom_inv64x
Xinv_boostn boostn gd vreg_tx_drv boostn_bar custom_inv64x
XI69 gd vreg_tx_drv sc_lvt_fill_6poly
XI68<0> gd vreg_tx_drv sc_lvt_decap_nf_4
XI68<1> gd vreg_tx_drv sc_lvt_decap_nf_4
