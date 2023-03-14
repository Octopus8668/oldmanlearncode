codist_set = [
    #Co-dist In_Folder   Processing_Folder  Archive_Folder   File_Ext File_Sequence Connection Loader_CtlFile Loader_Log_Folder Loader_Discard_Folder Loader_BadFile_Folder
    ['TMS', ['C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\TMS\\TMS_IN','C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\TMS\\PROCESSING','C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\TMS\\ARCHIVE','.csv','C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\TMS\\MISC\\TMS_Sequence.txt','webuser/aP#ss747@cgaprod','C:\\FTP\\CODIST\\TMS\\LOADER\\CTLFILE\\tms.ctl.txt','C:\\FTP\\CODIST\\TMS\\LOADER\\LOG','C:\\FTP\\CODIST\\TMS\\LOADER\\DISCARD','C:\\FTP\\CODIST\\TMS\\LOADER\\BADFILE'], ['pktuy@vstv.vn','danhpt@tms.com.vn', 'huytq@tms.com.vn', 'ly.tran@vstv.vn', 'trithanh@vstv.vn','trqhuy123@yahoo.com.vn','bacbx@tms.com.vn','xuanbac1979@gmail.com'],'@C:\\FTP\\Python_Scripts\\run_TMS_CHECKDAILY.sql'],
    ['VTVC_POSTPAID', ['C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\VTVC\\VTVC_IN','C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\VTVC\\PROCESSING','C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\VTVC\\ARCHIVE','.csv','C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\VTVC\\MISC\\VTVC_Sequence.txt','webuser/aP#ss747@cgaprod','C:\\FTP\\CODIST\\VTVC\\LOADER\\CTLFILE\\vtvc.ctl.txt','C:\\FTP\\CODIST\\VTVC\\LOADER\\LOG','C:\\FTP\\CODIST\\VTVC\\LOADER\\DISCARD','C:\\FTP\\CODIST\\VTVC\\LOADER\\BADFILE'], ['ly.tran@vstv.vn', 'trithanh@vstv.vn','vananh7@vtvcab.vn','khactuy@vtvcab.vn','quanglam@vtvcab.vn'],'@C:\\FTP\\Python_Scripts\\run_VTVC_CHECKDAILY.sql'],
    ['VTVC_PREPAID', ['C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\VCTV\\VCTV_IN','C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\VCTV\\PROCESSING','C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\VCTV\\ARCHIVE','.csv','C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\VCTV\\MISC\\VCTV_Sequence.txt','webuser/aP#ss747@cgaprod','C:\\FTP\\CODIST\\VCTV\\LOADER\\CTLFILE\\vctv.ctl.txt','C:\\FTP\\CODIST\\VCTV\\LOADER\\LOG','C:\\FTP\\CODIST\\VCTV\\LOADER\\DISCARD','C:\\FTP\\CODIST\\VCTV\\LOADER\\BADFILE'], ['ly.tran@vstv.vn', 'trithanh@vstv.vn','vananh7@vtvcab.vn','khactuy@vtvcab.vn','quanglam@vtvcab.vn'],'@C:\\FTP\\Python_Scripts\\run_VCTV_CHECKDAILY.sql'],
    ['HCATV', ['C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\HCATV\\HCATV_IN','C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\HCATV\\PROCESSING','C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\HCATV\\ARCHIVE','.csv','C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\HCATV\\MISC\\HCATV_Sequence.txt','webuser/aP#ss747@cgaprod','C:\\FTP\\CODIST\\HCATV\\LOADER\\CTLFILE\\hcatv.ctl.txt','C:\\FTP\\CODIST\\HCATV\\LOADER\\LOG','C:\\FTP\\CODIST\\HCATV\\LOADER\\DISCARD','C:\\FTP\\CODIST\\HCATV\\LOADER\\BADFILE'], [ 'trithanh@vstv.vn','ly.tran@vstv.vn', 'vuanhduc@hanoicab.com.vn'], '@C:\\FTP\\Python_Scripts\\run_HCATV_CHECKDAILY.sql'],
    ['MYTV',   ['C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\MYTV\\MYTV_IN','C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\MYTV\\PROCESSING','C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\MYTV\\ARCHIVE','.csv','C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\MYTV\\MISC\\MYTV_Sequence.txt','webuser/aP#ss747@cgaprod','C:\\FTP\\CODIST\\MYTV\\LOADER\\CTLFILE\\mytv.ctl.txt','C:\\FTP\\CODIST\\MYTV\\LOADER\\LOG','C:\\FTP\\CODIST\\MYTV\\LOADER\\DISCARD','C:\\FTP\\CODIST\\MYTV\\LOADER\\BADFILE'], [ 'trithanh@vstv.vn','ly.tran@vstv.vn'], '@C:\\FTP\\Python_Scripts\\run_MYTV_CHECKDAILY.sql'],
    ['MYTVWS', ['C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\MYTV\\MYTV_IN','C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\MYTV\\PROCESSING','C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\MYTV\\ARCHIVE','.csv','C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\MYTV\\MISC\\MYTV_Sequence.txt','webuser/aP#ss747@cgaprod','C:\\FTP\\CODIST\\MYTV\\LOADER\\CTLFILE\\VN_WHOLESALE.ctl.txt','C:\\FTP\\CODIST\\MYTV\\LOADER\\LOG','C:\\FTP\\CODIST\\MYTV\\LOADER\\DISCARD','C:\\FTP\\CODIST\\MYTV\\LOADER\\BADFILE'], [ 'trithanh@vstv.vn'], '@C:\\FTP\\Python_Scripts\\run_VN_WHOLESALE_MERGE.sql'],
    ['FPTWS', ['C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\FPT\\FPT_IN','C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\FPT\\PROCESSING','C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\FPT\\ARCHIVE','.csv','C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\FPT\\MISC\\FPT_Sequence.txt','webuser/aP#ss747@cgaprod','C:\\FTP\\CODIST\\FPT\\LOADER\\CTLFILE\\VN_WHOLESALE.ctl.txt','C:\\FTP\\CODIST\\FPT\\LOADER\\LOG','C:\\FTP\\CODIST\\FPT\\LOADER\\DISCARD','C:\\FTP\\CODIST\\FPT\\LOADER\\BADFILE'], [ 'trithanh@vstv.vn','ly.tran@vstv.vn','NghiaNH4@FPT.COM.VN'], '@C:\\FTP\\Python_Scripts\\run_VN_WHOLESALE_MERGE.sql'],
    ['VTELWS', ['C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\VTEL\\VTEL_IN','C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\VTEL\\PROCESSING','C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\VTEL\\ARCHIVE','.csv','C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\VTEL\\MISC\\VTEL_Sequence.txt','webuser/aP#ss747@cgaprod','C:\\FTP\\CODIST\\VTEL\\LOADER\\CTLFILE\\VN_WHOLESALE_VTEL.ctl.txt','C:\\FTP\\CODIST\\VTEL\\LOADER\\LOG','C:\\FTP\\CODIST\\VTEL\\LOADER\\DISCARD','C:\\FTP\\CODIST\\VTEL\\LOADER\\BADFILE'], [ 'trithanh@vstv.vn'], '@C:\\FTP\\Python_Scripts\\run_VN_WHOLESALE_MERGE_VTEL.sql'],
    ['MOBIFONE', ['D:\\VNPAYMENT\\MOBIFONE\\MOBIFONE_IN','D:\\VNPAYMENT\\MOBIFONE\\PROCESSING','D:\\VNPAYMENT\\MOBIFONE\\ARCHIVE','.cdr','D:\\VNPAYMENT\\MOBIFONE\\MISC\\MOBIFONE_Sequence.txt','webuser/aP#ss747@cgaprod','D:\\VNPAYMENT\\MOBIFONE\\LOADER\\CTLFILE\\VN_PAYMENT_CDR_MBF30.ctl.txt','D:\\VNPAYMENT\\MOBIFONE\\LOADER\\LOG','D:\\VNPAYMENT\\MOBIFONE\\LOADER\\DISCARD','D:\\VNPAYMENT\\MOBIFONE\\LOADER\\BADFILE'], [ 'database@vstv.vn'], '@C:\\FTP\\Python_Scripts\\run_VN_PAYMENT_CDR_MBF30.sql'],
    ['Z4', ['C:\\FTP\\CGA\\FTP\\ROOT\\Z4_IN','C:\\FTP\\CGA\\FTP\\PROCESSING','C:\\FTP\\CGA\\FTP\\ARCHIVE','.csv','C:\\FTP\\CGA\\FTP\MISC\\CGA_Sequence.txt','webuser/aP#ss747@cgaprod','C:\\FTP\\CGA\\LOADER\\CTLFILE\\VN_PACK_NEWEQUIP_Z4.ctl.txt','C:\\FTP\\CGA\\LOADER\\LOG','C:\\FTP\\CGA\\LOADER\\DISCARD','C:\\FTP\\CGA\\LOADER\\BADFILE'], [ 'trithanh@vstv.vn'], '@C:\\FTP\\Python_Scripts\\run_IMP_Z4_X4.sql'],
    ['Z4_TEST', ['C:\\FTP\\CGA\\FTP\\ROOT\\TEST\\Z4_TEST_IN','C:\\FTP\\CGA\\FTP\\PROCESSING','C:\\FTP\\CGA\\FTP\\ARCHIVE_TEST','.csv','C:\\FTP\\CGA\\FTP\MISC\\CGA_Sequence.txt','webuser/webuser@cgadev','C:\\FTP\\CGA\\LOADER\\CTLFILE\\VN_PACK_NEWEQUIP_Z4.ctl.txt','C:\\FTP\\CGA\\LOADER\\LOG','C:\\FTP\\CGA\\LOADER\\DISCARD','C:\\FTP\\CGA\\LOADER\\BADFILE'], [ 'trithanh@vstv.vn'], '@C:\\FTP\\Python_Scripts\\run_IMP_Z4_X4.sql'],
    ['Z3NT', ['C:\\FTP\\CGA\\FTP\\ROOT\\Z3NT_IN','C:\\FTP\\CGA\\FTP\\PROCESSING','C:\\FTP\\CGA\\FTP\\ARCHIVE','.csv','C:\\FTP\\CGA\\FTP\MISC\\CGA_Sequence.txt','webuser/aP#ss747@cgaprod','C:\\FTP\\CGA\\LOADER\\CTLFILE\\VN_PACK_NEWEQUIP_Z3NT.ctl.txt','C:\\FTP\\CGA\\LOADER\\LOG','C:\\FTP\\CGA\\LOADER\\DISCARD','C:\\FTP\\CGA\\LOADER\\BADFILE'], [ 'trithanh@vstv.vn'], '@C:\\FTP\\Python_Scripts\\run_IMP_Z3NT.sql'],
    ['Z3NT_TEST', ['C:\\FTP\\CGA\\FTP\\ROOT\\TEST\\Z3NT_TEST_IN','C:\\FTP\\CGA\\FTP\\PROCESSING','C:\\FTP\\CGA\\FTP\\ARCHIVE_TEST','.csv','C:\\FTP\\CGA\\FTP\MISC\\CGA_Sequence.txt','webuser/webuser@cgadev','C:\\FTP\\CGA\\LOADER\\CTLFILE\\VN_PACK_NEWEQUIP_Z3NT.ctl.txt','C:\\FTP\\CGA\\LOADER\\LOG','C:\\FTP\\CGA\\LOADER\\DISCARD','C:\\FTP\\CGA\\LOADER\\BADFILE'], [ 'trithanh@vstv.vn'], '@C:\\FTP\\Python_Scripts\\run_IMP_Z3NT.sql'],
    ['MYTEST', ['C:\\Data\\VSTV\\Projects\\TMS\\CODIST\\FTP_FOLDERS\\IN\\HCATV\\HCATV_IN','C:\\Data\\VSTV\\Projects\\TMS\\CODIST\\FTP_FOLDERS\\IN\\HCATV\\HCATV_IN\\PROCESSING','C:\\Data\\VSTV\\Projects\\TMS\\CODIST\\FTP_FOLDERS\\IN\\HCATV\\HCATV_IN\\ARCHIVE','.csv','C:\\Data\\VSTV\\Projects\\TMS\\CODIST\\FTP_FOLDERS\\IN\\HCATV\\HCATV_IN\\MISC\\HCATV_Sequence.txt','webuser/webuser@dev_vstv','C:\\Data\\VSTV\\Projects\\TMS\\CODIST\\HCATV\\LOADER\\CTLFILE\\hcatv.ctl.txt','C:\\Data\\VSTV\\Projects\\TMS\\CODIST\\HCATV\\LOADER\\LOG','C:\\Data\\VSTV\\Projects\\TMS\\CODIST\\HCATV\\LOADER\\DISCARD','C:\\Data\\VSTV\\Projects\\TMS\\CODIST\\HCATV\\LOADER\\BADFILE'],[ 'ly.tran@vstv.vn', 'trithanh@vstv.vn'], 'C:\\FTP\\Python_Scripts\\run_TMS_CHECKDAILY.sql'],
    ['ASPROCESS', ['C:\\FTP\\CGA\\FTP\\ROOT\\ASPROCESS_IN','C:\\FTP\\CGA\\FTP\\PROCESSING','C:\\FTP\\CGA\\FTP\\ARCHIVE','.csv','C:\\FTP\\CGA\\FTP\MISC\\CGA_Sequence.txt','webuser/aP#ss747@cgaprod','C:\\FTP\\CGA\\LOADER\\CTLFILE\\VN_TEMP_AFTER_SALE.ctl.txt','C:\\FTP\\CGA\\LOADER\\LOG','C:\\FTP\\CGA\\LOADER\\DISCARD','C:\\FTP\\CGA\\LOADER\\BADFILE'], [ 'database@vstv.vn'], '@C:\\FTP\\Python_Scripts\\ASPROCESS.sql'],
    ['VTVCWS', ['C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\VTVC\\VTVC_IN','C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\VTVC\\PROCESSING','C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\VTVC\\ARCHIVE','.ws','C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\VTVC\\MISC\\VTVC_Sequence.txt','webuser/aP#ss747@cgaprod','C:\\FTP\\CODIST\\VTVC\\LOADER\\CTLFILE\\VTVC_VN_WHOLESALE.ctl.txt','C:\\FTP\\CODIST\\VTVC\\LOADER\\LOG','C:\\FTP\\CODIST\\VTVC\\LOADER\\DISCARD','C:\\FTP\\CODIST\\VTVC\\LOADER\\BADFILE'], ['database@vstv.vn'],'@C:\\FTP\\Python_Scripts\\run_VTVC_VN_WHOLESALE_MERGE.sql'],
    ['VIEON', ['C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\VIEON\\VIEON_IN','C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\VIEON\\PROCESSING','C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\VIEON\\ARCHIVE','.csv','C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\VIEON\\MISC\\VIEON_Sequence.txt','webuser/aP#ss747@cgaprod','C:\\FTP\\CODIST\\VIEON\\LOADER\\CTLFILE\\VIEON_VN_WHOLESALE.ctl.txt','C:\\FTP\\CODIST\\VIEON\\LOADER\\LOG','C:\\FTP\\CODIST\\VIEON\\LOADER\\DISCARD','C:\\FTP\\CODIST\\VIEON\\LOADER\\BADFILE'], ['database@vstv.vn'],'@C:\\FTP\\Python_Scripts\\run_VIEON_VN_WHOLESALE_MERGE.sql'],
    ['VIEON_BASIC', ['C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\VIEON\\VIEON_IN','C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\VIEON\\PROCESSING','C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\VIEON\\ARCHIVE','.csv','C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\VIEON\\MISC\\VIEON_Sequence.txt','webuser/aP#ss747@cgaprod','C:\\FTP\\CODIST\\VIEON\\LOADER\\CTLFILE\\VIEON_VN_WHOLESALE.ctl.txt','C:\\FTP\\CODIST\\VIEON\\LOADER\\LOG','C:\\FTP\\CODIST\\VIEON\\LOADER\\DISCARD','C:\\FTP\\CODIST\\VIEON\\LOADER\\BADFILE'], ['database@vstv.vn'],'@C:\\FTP\\Python_Scripts\\run_VIEON_BASIC_VN_WHOLESALE_MERGE.sql'],
    ['APPLE', ['C:\\FTP\CODIST\\FTP_FOLDERS\\IN\\OTT\\IN\\APPLE','C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\OTT\\PROCESSING','C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\OTT\\ARCHIVE\\APPLE','.csv','C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\OTT\\MISC\\APPLE_Sequence.txt','webuser/aP#ss747@cgaprod','C:\\FTP\\CODIST\\OTT\\LOADER\\CTLFILE\\VN_INAPP_PAYMENT_APPLE.ctl.txt','C:\\FTP\\CODIST\\OTT\\LOADER\\LOG','C:\\FTP\\CODIST\\OTT\\LOADER\\DISCARD','C:\\FTP\\CODIST\\OTT\\LOADER\\BADFILE'], ['trithanh@vstv.vn'],'@C:\\FTP\\Python_Scripts\\run_APPLE_SALEREPORT_MERGE.sql'],
    ['GOOGLE', ['C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\OTT\\IN\\GOOGLE','C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\OTT\\PROCESSING','C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\OTT\\ARCHIVE\\GOOGLE','.csv','C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\OTT\\MISC\\GOOGLE_Sequence.txt','webuser/aP#ss747@cgaprod','C:\\FTP\\CODIST\\OTT\\LOADER\\CTLFILE\\VN_INAPP_PAYMENT_GOOLE.ctl.txt','C:\\FTP\\CODIST\\OTT\\LOADER\\LOG','C:\\FTP\\CODIST\\OTT\\LOADER\\DISCARD','C:\\FTP\\CODIST\\OTT\\LOADER\\BADFILE'], ['trithanh@vstv.vn'],'@C:\\FTP\\Python_Scripts\\run_GOOGLE_SALEREPORT_MERGE.sql'],
    ['MyTV_OTT_WS', ['C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\MYTV\\MYTV_IN','C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\MYTV\\PROCESSING','C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\MYTV\\ARCHIVE','.csv','C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\MYTV\\MISC\\MYTV_Sequence.txt','webuser/aP#ss747@cgaprod','C:\\FTP\\CODIST\\MYTV\\LOADER\\CTLFILE\\VN_WHOLESALE_MyTV_OTT.ctl.txt','C:\\FTP\\CODIST\\MYTV\\LOADER\\LOG','C:\\FTP\\CODIST\\MYTV\\LOADER\\DISCARD','C:\\FTP\\CODIST\\MYTV\\LOADER\\BADFILE'], [ 'trithanh@vstv.vn'], '@C:\\FTP\\Python_Scripts\\run_VN_WHOLESALE_MERGE.sql'],
    ['MyTV_MOBILE_WS', ['C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\MYTV\\MYTV_IN','C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\MYTV\\PROCESSING','C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\MYTV\\ARCHIVE','.csv','C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\MYTV\\MISC\\MYTV_Sequence.txt','webuser/aP#ss747@cgaprod','C:\\FTP\\CODIST\\MYTV\\LOADER\\CTLFILE\\VN_WHOLESALE_MyTV_MOBILE.ctl.txt','C:\\FTP\\CODIST\\MYTV\\LOADER\\LOG','C:\\FTP\\CODIST\\MYTV\\LOADER\\DISCARD','C:\\FTP\\CODIST\\MYTV\\LOADER\\BADFILE'], [ 'trithanh@vstv.vn'], '@C:\\FTP\\Python_Scripts\\run_VN_WHOLESALE_MERGE.sql'],
# DEV    ['APPLE', ['C:\\FTP\CODIST\\FTP_FOLDERS\\IN\\OTT\\IN\\APPLE','C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\OTT\\PROCESSING','C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\OTT\\ARCHIVE\\APPLE','.csv','C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\OTT\\MISC\\APPLE_Sequence.txt','webuser/webuser@cgadev','C:\\FTP\\CODIST\\OTT\\LOADER\\CTLFILE\\VN_INAPP_PAYMENT_APPLE.ctl.txt','C:\\FTP\\CODIST\\OTT\\LOADER\\LOG','C:\\FTP\\CODIST\\OTT\\LOADER\\DISCARD','C:\\FTP\\CODIST\\OTT\\LOADER\\BADFILE'], ['trithanh@vstv.vn'],'@C:\\FTP\\Python_Scripts\\run_APPLE_SALEREPORT_MERGE.sql'],
# DEV   ['GOOGLE', ['C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\OTT\\IN\\GOOGLE','C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\OTT\\PROCESSING','C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\OTT\\ARCHIVE\\GOOGLE','.csv','C:\\FTP\\CODIST\\FTP_FOLDERS\\IN\\OTT\\MISC\\GOOGLE_Sequence.txt','webuser/webuser@cgadev','C:\\FTP\\CODIST\\OTT\\LOADER\\CTLFILE\\VN_INAPP_PAYMENT_GOOLE.ctl.txt','C:\\FTP\\CODIST\\OTT\\LOADER\\LOG','C:\\FTP\\CODIST\\OTT\\LOADER\\DISCARD','C:\\FTP\\CODIST\\OTT\\LOADER\\BADFILE'], ['trithanh@vstv.vn'],'@C:\\FTP\\Python_Scripts\\run_GOOGLE_SALEREPORT_MERGE.sql'],
]