label delete_me_soon:
    python:
        import time
        import sys
        from watchdog.observers import Observer
        from watchdog.events import PatternMatchingEventHandler
        import glob
        import os

        class MyHandler(PatternMatchingEventHandler):
            patterns = ["*.py"]

            def process(self, event):
                print(event.src_path, event.event_type)

            def on_modified(self, event):
                self.process(event)

            def on_created(self, event):
                self.process(event)

            def on_deleted(self, event):
                '''
                Can we make this more safe? Like, idk, it seems dodgy or unsafe to delete all text files,
                Also, the hard-coded path to Collette's local files needs to be generalized
                '''
                filelist=glob.glob("/Users/princesssteffykins/Desktop/Managed_Memory/*.txt")
                filelist.sort(reverse=True)
                for file in filelist:
                    time.sleep(1)
                    os.remove(file)
                self.process(event)

        if __name__ == '__main__':
            args = sys.argv[1:]
            observer = Observer()
            observer.schedule(MyHandler(), path=args[0] if args else '.')
            observer.start()

            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                observer.stop()

            observer.join()
