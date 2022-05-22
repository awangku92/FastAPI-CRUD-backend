import os, logging as lg

def custom_log(log_lvl, str_log):
	path = os.path.join(os.getcwd(), 'FastAPIlog.log')

	if log_lvl == 'info':
		lg.basicConfig(filename=path, level=lg.INFO, format='%(asctime)s  %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
		lg.info('Starting API service')

	if log_lvl == 'error':
		lg.basicConfig(filename=path, level=lg.ERROR, format='%(asctime)s  %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
		lg.error(str_log)