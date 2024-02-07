
|Level|When it’s used|
|---|---|
|`DEBUG`|Detailed information, typically of interest only when diagnosing problems.|
|`INFO`|Confirmation that things are working as expected.|
|`WARNING`|An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.|
|`ERROR`|Due to a more serious problem, the software has not been able to perform some function.|
|`CRITICAL`|A serious error, indicating that the program itself may be unable to continue running.|
`**logging.BasicConfig(**kwargs)**`:
set up the logging:
**filename** - log to specified file
**filemode** - open filename in this mode. Default is 'a'
**format** - Use the specified format string for the handler. Defaults to attributes `levelname`, `name` and `message` separated by colons.
**datefmt** - Use the specified date/time format, as accepted by `time.strftime()`.
**style** - If _format_ is specified, use this style for the format string. One of `'%'`, `'{'` or `'$'` for printf-style, `str.format()` or `string.Template` respectively. Defaults to `'%'`.
**level** - Set the root logger level to the specified level. Logs all events of that level or below in the table above.
**stream** - Use the specified stream to initialize the `StreamHandler`. Note that this argument is incompatible with _filename_ - if both are present, a `ValueError` is raised.
**handlers** - If specified, this should be an iterable of already created handlers to add to the root logger. Any handlers which don’t already have a formatter set will be assigned the default formatter created in this function. Note that this argument is incompatible with _filename_ or _stream_ - if both are present, a `ValueError` is raised.
**force** - If this keyword argument is specified as true, any existing handlers attached to the root logger are removed and closed, before carrying out the configuration as specified by the other arguments.
**encoding** - If this keyword argument is specified along with _filename_, its value is used when the `FileHandler` is created, and thus used when opening the output file.
**errors** - If this keyword argument is specified along with _filename_, its value is used when the `FileHandler` is created, and thus used when opening the output file. If not specified, the value ‘backslashreplace’ is used. Note that if `None` is specified, it will be passed as such to `open()`, which means that it will be treated the same as passing ‘errors’.

**logging.shutdown()**
Informs the logging system to perform an orderly shutdown by flushing and closing all handlers. This should be called at application exit and no further use of the logging system should be made after this call.
When the logging module is imported, it registers this function as an exit handler (see `atexit`), so normally there’s no need to do that manually.

creating a logger:
`logger = logging.getLogger(__name__)`

These loggers have to be configured separately, as basicConfig only configures the root logger.

![[Logging.png]]

Create custom loggers with names, but do not add handlers, so that the message propagates up to root, allowing root handlers to deal with it.