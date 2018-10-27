from ont_fast5_api.fast5_file import Fast5File
f = Fast5File("test.fast5", "r+")
 f.set_tracking_id({}, clear=True)
