
***************************************************************************
*** SS7 LPP LVS INCLUDE FILE
***************************************************************************
*.SCALE METER 
*.LENGTH_UNIT CPP
*.LENGTH_UNIT FPITCH
*.NON_UNIT PBAR
*.LENGTH_UNIT SAC
*.LENGTH_UNIT sac_c sac_p

.subckt alias1 plus minus w=0 l=0
ralias plus minus M1_lvsres w=w l=l rval=0.001
.ends

.subckt alias2 plus minus w=0 l=0
ralias plus minus M2_lvsres w=w l=l rval=0.001
.ends

.subckt alias3 plus minus w=0 l=0
ralias plus minus M3_lvsres w=w l=l rval=0.001
.ends

.subckt alias4 plus minus w=0 l=0
ralias plus minus M4_lvsres w=w l=l rval=0.001
.ends

.subckt alias5 plus minus w=0 l=0
ralias plus minus D5_lvsres w=w l=l rval=0.001
.ends

.subckt alias6 plus minus w=0 l=0
ralias plus minus D6_lvsres w=w l=l rval=0.001
.ends

.subckt alias7 plus minus w=0 l=0
ralias plus minus D7_lvsres w=w l=l rval=0.001
.ends

.subckt alias8 plus minus w=0 l=0
ralias plus minus D8_lvsres w=w l=l rval=0.001
.ends

.subckt alias9 plus minus w=0 l=0
ralias plus minus D9_lvsres w=w l=l rval=0.001
.ends

.subckt alias10 plus minus w=0 l=0
ralias plus minus D10_lvsres w=w l=l rval=0.001
.ends

.subckt alias11 plus minus w=0 l=0
ralias plus minus D11_lvsres w=w l=l rval=0.001
.ends

.subckt alias12 plus minus w=0 l=0
ralias plus minus IA_lvsres w=w l=l rval=0.001
.ends

.subckt alias13 plus minus w=0 l=0
ralias plus minus IB_lvsres w=w l=l rval=0.001
.ends

.subckt aliasmtop_1 plus minus w=0 l=0
ralias plus minus IA_lvsres w=w l=l rval=0.001
.ends

.subckt aliasmtop plus minus w=0 l=0
ralias plus minus IB_lvsres w=w l=l rval=0.001
.ends

.subckt aliasrdl plus minus l=l w=w
ralias plus minus LB_lvsres l=l w=w rval=0.001
.ends

.subckt aliasap plus minus l=l w=w
ralias plus minus LB_lvsres l=l w=w rval=0.001
.ends

.SUBCKT vncap_2t A B
.ENDS

.subckt esdnsh d g s b 
.ends esdnsh


.subckt esdnsh_stk d g1 g2 s b
.ends esdnsh_stk

***************************************************************************
*Custom Compiler Version N-2017.12-SP1-6
*Thu Nov 15 08:11:53 2018

*.SCALE METER
*.LDD

********************************************************************************
* Library          : c10_gold
* Cell             : tx_vdriver_mos_drv
* View             : schematic
* View Search List : auCdl schematic symbol
* View Stop List   :
********************************************************************************
.subckt tx_vdriver_mos_drv a drv_en drv_en_n gd n p vreg_tx_drv
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
.ends tx_vdriver_mos_drv

********************************************************************************
* Library          : c10_gold
* Cell             : tx_vdriver_down_full_boost
* View             : schematic
* View Search List : auCdl schematic symbol
* View Stop List   :
********************************************************************************
.subckt tx_vdriver_down_full_boost boostn bpass drv_en gd ndrv nout
*.PININFO boostn:I bpass:B drv_en:I gd:B ndrv:I nout:B
Mn_sw2 n_mid boostn bpass gd lvtnfet l=8n nf=1 nfin=8 fpitch=0.027u m=8 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
Mn_sw1 nout drv_en n_mid gd lvtnfet l=8n nf=1 nfin=8 fpitch=0.027u m=8 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
Mn_sw_dm_ gd gd gd gd lvtnfet l=8n nf=1 nfin=8 fpitch=0.027u m=6 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
Mn_sw n_mid ndrv gd gd lvtnfet l=8n nf=1 nfin=8 fpitch=0.027u m=6 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
.ends tx_vdriver_down_full_boost

********************************************************************************
* Library          : c10_gold
* Cell             : tx_vdriver_res_full_boost
* View             : schematic
* View Search List : auCdl schematic symbol
* View Stop List   :
********************************************************************************
.subckt tx_vdriver_res_full_boost gd mid_dn mid_up pre_r vout
*.PININFO gd:B mid_dn:B mid_up:B pre_r:B vout:B
rRfix_par2 pre_r mid_dn rmres w=1.32u l=1.7u r=673.962 rmdir=2 drawfill=0 m=1 pbar=1 sbar=1 orientation=2 r_cut=0 ncr=2 $SUB=gd
rRfix_par4 mid_dn vout rmres w=1.32u l=1.7u r=673.962 rmdir=2 drawfill=0 m=1 pbar=1 sbar=1 orientation=2 r_cut=0 ncr=2 $SUB=gd
rRfix_par1 mid_up vout rmres w=1.32u l=1.7u r=673.962 rmdir=2 drawfill=0 m=1 pbar=1 sbar=1 orientation=2 r_cut=0 ncr=2 $SUB=gd
rRfix_par0 pre_r mid_up rmres w=1.32u l=1.7u r=673.962 rmdir=2 drawfill=0 m=1 pbar=1 sbar=1 orientation=2 r_cut=0 ncr=2 $SUB=gd
.ends tx_vdriver_res_full_boost

********************************************************************************
* Library          : c10_gold
* Cell             : tx_vdriver_up_full_boost
* View             : schematic
* View Search List : auCdl schematic symbol
* View Stop List   :
********************************************************************************
.subckt tx_vdriver_up_full_boost boostp bpass drv_en_n pdrv pout vreg_tx_drv
*.PININFO boostp:I bpass:B drv_en_n:I pdrv:I pout:B vreg_tx_drv:B
Mp_sw1 pout drv_en_n p_mid vreg_tx_drv lvtpfet l=8n nf=1 nfin=8 fpitch=0.027u m=12 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
Mp_sw p_mid pdrv vreg_tx_drv vreg_tx_drv lvtpfet l=8n nf=1 nfin=8 fpitch=0.027u m=6 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
Mp_sw2 bpass boostp p_mid vreg_tx_drv lvtpfet l=8n nf=1 nfin=8 fpitch=0.027u m=8 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
.ends tx_vdriver_up_full_boost

********************************************************************************
* Library          : c10_gold
* Cell             : tx_vdriver_mos_full
* View             : schematic
* View Search List : auCdl schematic symbol
* View Stop List   :
********************************************************************************
.subckt tx_vdriver_mos_full boostn boostp data_serial drv_en drv_en_n gd vout vreg_tx_drv
*.PININFO boostn:I boostp:I data_serial:I drv_en:I drv_en_n:I gd:B vout:B vreg_tx_drv:B
Xdrv data_serial drv_en drv_en_n gd ndrv pdrv vreg_tx_drv tx_vdriver_mos_drv
Xpdn boostn bpass_dn drv_en gd ndrv pre_r tx_vdriver_down_full_boost
Xres_full gd bpass_dn bpass_up pre_r vout tx_vdriver_res_full_boost
xI79 pre_r vflag v=0.75
xI77 vout vflag v=0.75
xI76 pre_r vflag v=0.75
Xpup boostp bpass_up drv_en_n pdrv pre_r vreg_tx_drv tx_vdriver_up_full_boost
.ends tx_vdriver_mos_full

********************************************************************************
* Library          : c10_gold
* Cell             : custom_inv64x
* View             : schematic
* View Search List : auCdl schematic symbol
* View Stop List   :
********************************************************************************
.subckt custom_inv64x a gd vp z
*.PININFO a:I gd:B vp:B z:O
MM0 z a gd gd lvtnfet l=8n nf=1 nfin=8 fpitch=0.027u m=4 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
MM1 z a vp vp lvtpfet l=8n nf=1 nfin=8 fpitch=0.027u m=4 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
.ends custom_inv64x

********************************************************************************
* Library          : sc_lvt
* Cell             : sc_lvt_fill_6poly
* View             : schematic
* View Search List : auCdl schematic symbol
* View Stop List   :
********************************************************************************
.subckt sc_lvt_fill_6poly gd vp
*.PININFO gd:B vp:B
MN1 gd gd gd gd lvtnfet l=8n nf=1 nfin=4 fpitch=0.027u m=4 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
MP2 vp vp vp vp lvtpfet l=8n nf=1 nfin=4 fpitch=0.027u m=4 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
.ends sc_lvt_fill_6poly

********************************************************************************
* Library          : sc_lvt
* Cell             : sc_lvt_decap_nf_4
* View             : schematic
* View Search List : auCdl schematic symbol
* View Stop List   :
********************************************************************************
.subckt sc_lvt_decap_nf_4 gd vp
*.PININFO gd:B vp:B
MP4 net10 net10 net10 vp lvtpfet l=8n nf=1 nfin=5 fpitch=0.027u m=2 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
MP0 vp net11 vp vp lvtpfet l=8n nf=1 nfin=5 fpitch=0.027u m=4 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
MM1 net10 net11 vp vp lvtpfet l=8n nf=1 nfin=5 fpitch=0.027u m=1 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
MN1 gd net10 net11 gd lvtnfet l=8n nf=1 nfin=5 fpitch=0.027u m=1 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
MN5 net11 net11 net11 gd lvtnfet l=8n nf=1 nfin=5 fpitch=0.027u m=2 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
MM0 gd net10 gd gd lvtnfet l=8n nf=1 nfin=5 fpitch=0.027u m=4 cpp=60n p_la=0 plorient=0 ptwell=0 ngcon=1 composite=0 wimpy_sw=0
.ends sc_lvt_decap_nf_4

********************************************************************************
* Library          : c10_gold
* Cell             : tx_vdriver_pair_full
* View             : schematic
* View Search List : auCdl schematic symbol
* View Stop List   :
********************************************************************************
.subckt tx_vdriver_pair_full boostn boostp data_ser_m data_ser_p drv_en drv_en_n gd tx_m tx_p vreg_tx_drv
*.PININFO boostn:I boostp:I data_ser_m:I data_ser_p:I drv_en:I drv_en_n:I gd:B tx_m:B tx_p:B vreg_tx_drv:B
Xdrv_p boostn_bar boostp_bar data_ser_p drv_en drv_en_n gd tx_p vreg_tx_drv tx_vdriver_mos_full
Xdrv_m boostn_bar boostp_bar data_ser_m drv_en drv_en_n gd tx_m vreg_tx_drv tx_vdriver_mos_full
Xinv_boostp boostp gd vreg_tx_drv boostp_bar custom_inv64x
Xinv_boostn boostn gd vreg_tx_drv boostn_bar custom_inv64x
XI69 gd vreg_tx_drv sc_lvt_fill_6poly
XI68<0> gd vreg_tx_drv sc_lvt_decap_nf_4
XI68<1> gd vreg_tx_drv sc_lvt_decap_nf_4
.ends tx_vdriver_pair_full


* START_SNAP_HIER
***********************************************************************************
**** This File Contains Report for Full Hierarchy of the Design ****
*******************************Please DO NOT DELETE********************************
* P4PORT=p4p-de02:1999; P4CLIENT=artakh_de02; USER=artakh; DATE=Thu Nov 15 07:11:54 UTC 2018
********************************************************************
**** snapHier.txt: //wwcad/msip/projects/c10/n208-c10-ss7lpp-18-ns/latest/lib/c10_gold/tx_vdriver_pair_full/snapHier/snapHier.txt#4
*******************************Please DO NOT DELETE********************************
* END_SNAP_HIER
***********************************************************************************
**** This Section Contains P4 Revision Report for Full Hierarchy of the Design ****
*******************************Please DO NOT DELETE********************************
***********************************************************************************
**** P4PORT=p4p-de02:1999 P4CLIENT=artakh_de02 USER=artakh DATE=15/11/18 08:12 +0100 *****
***********************************************************************************
** libName/cellName/viewName Revision Changelist Date Md5sum DepotFile
***********************************************************************************
* analogLib/cap/symbol --/-- -- -- 3d2676c6d1142457d056db14c718641f --
* analogLib/pcapacitor/symbol --/-- -- -- b4de1836ed113fd410917087d01df708 --
* vflags/vflag/layout --/-- -- -- 1581d9757f8ec31c0abfc9cc42271bca --
* vflags/vflag/symbol --/-- -- -- 0ef8a66dabb870eb1382ae0c8e3192ab --
* widgets/dspfcap/schematic --/-- -- -- 06259557961ac15f4b116793ce2adf55 --
* widgets/wire_cap/schematic --/-- -- -- 34bbe1feadaa9b0716c7934a6dc07ded --
* devices/nfinlvt/symbol --/-- -- -- fb08035224877c800202c94cb6a48b05 --
* devices/nfinulvt/symbol --/-- -- -- 41028b12440774dcc48ba75872e2df15 --
* devices/pfinlvt/symbol --/-- -- -- 150c9ef9a93f7fe649249ee394d2d776 --
* devices/pfinulvt/symbol --/-- -- -- d16ba8c3230eca6e36aef9bf7c58b7d4 --
* devices/rppwl/symbol --/-- -- -- 2b56802f61620faa333f0c76d10c18a6 --
* sc_lvt/sc_lvt_decap_nf_4/layout 1/1 3493255 26/06/18 06:27 dba09327b313d2bb0fadaa00565fb9b8 //wwcad/msip/common_libs/sc/ss7lpp/release/rel3.01/sc_lvt/sc_lvt_decap_nf_4/layout/layout.oa
* sc_lvt/sc_lvt_decap_nf_4/schematic 1/1 3493255 26/06/18 06:27 c76c4dd81b5805b21b1d1ea08e3b6401 //wwcad/msip/common_libs/sc/ss7lpp/release/rel3.01/sc_lvt/sc_lvt_decap_nf_4/schematic/sch.oa
* sc_lvt/sc_lvt_fill_6poly/layout 1/1 3493255 26/06/18 06:27 4ffd1b560f11076464065fd061bc27a4 //wwcad/msip/common_libs/sc/ss7lpp/release/rel3.01/sc_lvt/sc_lvt_fill_6poly/layout/layout.oa
* sc_lvt/sc_lvt_fill_6poly/schematic 1/1 3493255 26/06/18 06:27 4311962ba80262aa3d7898d931c29b40 //wwcad/msip/common_libs/sc/ss7lpp/release/rel3.01/sc_lvt/sc_lvt_fill_6poly/schematic/sch.oa
* c10_gold/custom_inv64x/layout 8/8 3568303 27/07/18 12:23 1b39f31ea14f0c39d932925d1c875805 //wwcad/msip/projects/c10/n208-c10-ss7lpp-18-ns/latest/lib/c10_gold/custom_inv64x/layout/layout.oa
* c10_gold/custom_inv64x/schematic 4/4 3444204 01/06/18 09:07 16263f9bd22f80d8ff03968abb033b94 //wwcad/msip/projects/c10/n208-c10-ss7lpp-18-ns/latest/lib/c10_gold/custom_inv64x/schematic/sch.oa
* c10_gold/tx_vdriver_down_full_boost/layout 26/26 3722296 03/10/18 05:13 888804b33276d9808c13bcc4972ecef3 //wwcad/msip/projects/c10/n208-c10-ss7lpp-18-ns/latest/lib/c10_gold/tx_vdriver_down_full_boost/layout/layout.oa
* c10_gold/tx_vdriver_down_full_boost/schematic 4/4 3712356 28/09/18 11:44 3619ab49ab59bf78aae72cf286a17748 //wwcad/msip/projects/c10/n208-c10-ss7lpp-18-ns/latest/lib/c10_gold/tx_vdriver_down_full_boost/schematic/sch.oa
* c10_gold/tx_vdriver_mos_drv/layout 22/22 3672823 14/09/18 10:16 3098eeaf107833ecff191678f8913571 //wwcad/msip/projects/c10/n208-c10-ss7lpp-18-ns/latest/lib/c10_gold/tx_vdriver_mos_drv/layout/layout.oa
* c10_gold/tx_vdriver_mos_drv/schematic 6/6 3635889 30/08/18 10:25 c02247391ad95e9eabc5004267a6c56c //wwcad/msip/projects/c10/n208-c10-ss7lpp-18-ns/latest/lib/c10_gold/tx_vdriver_mos_drv/schematic/sch.oa
* c10_gold/tx_vdriver_mos_full/layout 29/29 3679846 18/09/18 03:18 c639e238cc0bc6677a315073d4a59b0b //wwcad/msip/projects/c10/n208-c10-ss7lpp-18-ns/latest/lib/c10_gold/tx_vdriver_mos_full/layout/layout.oa
* c10_gold/tx_vdriver_mos_full/schematic 7/7 3635889 30/08/18 10:25 47380baf9b80a1443cac068ca85b912f //wwcad/msip/projects/c10/n208-c10-ss7lpp-18-ns/latest/lib/c10_gold/tx_vdriver_mos_full/schematic/sch.oa
* c10_gold/tx_vdriver_pair_full/layout 28/28 3732927 05/10/18 10:27 1c9bdc637ed11df0f5511ce7116cfbfb //wwcad/msip/projects/c10/n208-c10-ss7lpp-18-ns/latest/lib/c10_gold/tx_vdriver_pair_full/layout/layout.oa
* c10_gold/tx_vdriver_pair_full/schematic 5/5 3537151 13/07/18 04:09 0dc643ccb42a2e5db5832708ff5aebcc //wwcad/msip/projects/c10/n208-c10-ss7lpp-18-ns/latest/lib/c10_gold/tx_vdriver_pair_full/schematic/sch.oa
* c10_gold/tx_vdriver_res_full_boost/layout 28/28 3815820 31/10/18 02:20 1186f5882e17d3dfd0e3d8292349bbbc //wwcad/msip/projects/c10/n208-c10-ss7lpp-18-ns/latest/lib/c10_gold/tx_vdriver_res_full_boost/layout/layout.oa
* c10_gold/tx_vdriver_res_full_boost/schematic 7/7 3815769 31/10/18 02:12 d4aefe354d1b1afe3ad59bb20425d853 //wwcad/msip/projects/c10/n208-c10-ss7lpp-18-ns/latest/lib/c10_gold/tx_vdriver_res_full_boost/schematic/sch.oa
* c10_gold/tx_vdriver_up_full_boost/layout 34/34 3856962 14/11/18 08:47 8cc3023dd128d40c1840b06f146f86cc //wwcad/msip/projects/c10/n208-c10-ss7lpp-18-ns/latest/lib/c10_gold/tx_vdriver_up_full_boost/layout/layout.oa
* c10_gold/tx_vdriver_up_full_boost/schematic 8/8 3857886 14/11/18 11:13 cbf506e7eea677655ee2839d44a1c5f7 //wwcad/msip/projects/c10/n208-c10-ss7lpp-18-ns/latest/lib/c10_gold/tx_vdriver_up_full_boost/schematic/sch.oa
* ------------------------------------------------> FILE END <------------------------------------------------
* FILE_INTEGRITY_SHA512: ce2f57f8a6003500aefb955a944779e534d3fd3d458c6b5bcb85c85873b0c764e54ba137ce81ff2dbec634cf041fcce9e97306e722faaf338fd2f3a289b3077e tx_vdriver_pair_full_ss7lpp.sp
