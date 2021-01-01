# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 21:53:00 2018

@author: A
"""

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