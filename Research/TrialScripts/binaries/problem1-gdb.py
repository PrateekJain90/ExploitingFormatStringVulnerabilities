import gdb

class CheckFmtBreakpoint(gdb.Breakpoint):


	def __init__(self, spec):
		super(CheckFmtBreakpoint, self).__init__(
			spec, gdb.BP_BREAKPOINT, internal=False
		)
		gdb.events.exited.connect(lambda x : gdb.execute("quit"))
		gdb.execute('r AA')

	def stop(self):

		gdb.execute('set logging overwrite on')		
		gdb.execute('set logging on')		
		for i in range(0,10):
			gdb.execute('x/s *((char **)environ+%d)'%i)
			gdb.execute('set logging off')		
			gdb.execute('set logging overwrite off')
			gdb.execute('set logging on')		

		gdb.execute('set logging off')		

		proc_map = [];
		with open("/proc/%d/maps" % gdb.selected_inferior().pid) as fp:
			f = open( 'procMap.txt', 'w' )
			f.write(fp.read())
	

CheckFmtBreakpoint("main")
