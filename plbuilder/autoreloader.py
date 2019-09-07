import os
import traceback
import inotify.adapters
from plbuilder.builder import build_by_file_path

# extensions of the files that need to be tracked
TRACKED_FILE_TYPES = ('.py',)

# inotify event types to accept
CHANGE_EVENTS = ["IN_MOVED_TO", "IN_MODIFY"]


def autobuild():
    """
    Starts a process which watches for file system events on sources in the current pl-builder project, and
    automatically builds sources in response to changes.
    """
    from plbuild.paths import SOURCE_PATH
    autobuild_at_path(SOURCE_PATH)


def autobuild_at_path(watch_path: str):
    # setting up inotify and specifying path to watch
    print(f'Starting autobuilder, watching for changes in {watch_path}')
    inotify_tree = inotify.adapters.InotifyTree(watch_path)

    for event in inotify_tree.event_gen():
        if event is not None:
            header, type_names, folder, filename = event
            if any(x in type_names for x in CHANGE_EVENTS) and filename.endswith(TRACKED_FILE_TYPES):
                file_path = os.path.join(folder, filename)
                try:
                    build_by_file_path(file_path)
                except Exception as e:
                    print(traceback.format_exc())
                    print(f'Could not complete build for {filename} due to {e.__class__.__name__}: {e}')
