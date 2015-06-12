from __future__ import absolute_import
from twisted.internet import reactor

# Note that if you're adding a new profiling method, please do the
# imports inside the _setup_*() method so the requirements remains
# optional


def _setup_theseus(fname):
    """
    Profiling via twisted-theseus; also needs Cython.
    """
    from theseus import Tracer
    t = Tracer()
    t.install()
    def write_profile():
        print("Writing profiling data to '{}'.".format(fname))
        with open(fname, 'w') as f:
            t.write_data(f)
    reactor.addSystemEventTrigger('before', 'shutdown', write_profile)


def _setup_vmprof(fname):
    """
    Setup profiling via 'vmprof'
    """
    import vmprof
    prof_fd = open(fname, 'w')
    vmprof.enable(prof_fd.fileno())
    print("Writing profiling data to '{}'.".format(fname))
    #reactor.addSystemEventTrigger('after', 'shutdown', vmprof.disable)


def _setup_profile(fname):
    import pstats
    pr = profile.Profile()
    pr.enable()
    def write_profile():
        #pr.disable()
        st = pstats.Stats(pr, stream=open(fname, 'w'))
        st.sort_stats('cumulative')
        st.print_stats()
    reactor.addSystemEventTrigger('after', 'shutdown', write_profile)


#: this is the only public API, see crossbar/worker/router.py for example
profilers = dict(
    theseus=_setup_theseus,
    vmprof=_setup_vmprof,
)
