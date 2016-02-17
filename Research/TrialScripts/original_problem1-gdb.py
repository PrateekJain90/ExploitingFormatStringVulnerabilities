import gdb

class CheckFmtBreakpoint(gdb.Breakpoint):

	def __init__(self, spec, fmt_idx):
		super(CheckFmtBreakpoint, self).__init__(
			spec, gdb.BP_BREAKPOINT, internal=False
		)
		self.fmt_idx = fmt_idx
		#gdb.execute('r hi')

	def stop(self):

		args = ["$ebp+8"]
		fmt_addr = gdb.parse_and_eval(args[self.fmt_idx])
		proc_map = []
		with open("/proc/%d/maps" % gdb.selected_inferior().pid) as fp:
			proc_map = self._parse_map(fp.read())

		for mapping in proc_map:
			if mapping["start"] <= fmt_addr < mapping["end"]:
				break
		else:
			print("%08x belongs to an unknown memory range" % fmt_addr)
			return True

		if "w" in mapping["perms"]:
			print("Format string in writable memory!")
			#gdb.execute('set logging off')	
			#gdb.execute('set logging on')	
			#gdb.execute('set logging overwrite on')	
			gdb.execute('bt -1')
			return True
			#gdb.execute('quit')

		return False

	def _parse_map(self, file_contents):

		zones = []
		for line in file_contents.split('\n'):
			if not line:
				continue
			memrange, perms, _ = line.split(None, 2)
			start, end = memrange.split('-')
			zones.append({
				'start': int(start, 16),
				'end': int(end, 16),
				'perms': perms
			})
		return zones

CheckFmtBreakpoint("printf", 0)
'''
CheckFmtBreakpoint("fprintf", 1)
CheckFmtBreakpoint("sprintf", 1)
CheckFmtBreakpoint("snprintf", 2)
CheckFmtBreakpoint("vprintf", 0)
CheckFmtBreakpoint("vfprintf", 1)
CheckFmtBreakpoint("vsprintf", 1)
CheckFmtBreakpoint("vsnprintf", 2)
'''
