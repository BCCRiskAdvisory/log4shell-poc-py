# log4shell-poc-py
POC for detecting the Log4Shell (Log4J RCE) vulnerability.

Run on a system with python3
`python3 log4shell-poc.py <pathToTargetFile> <InteractionURL>`

- `pathToTargetFile` - containing a list of targets (targets are seperated by newlines)
- `InteractionURL` - the endpoint used to monitor out of band data extraction or interactions, e.g: https://github.com/projectdiscovery/interactsh


### Example Output

```
[1] Testing asset: http://<target_address1>

[2] Testing asset: http://<target_address2>

[3] Testing asset: http://<target_address3>

[4] Testing asset: http://<target_address4>

[5] Testing asset: http://<target_address5>

[6] Testing asset: http://<target_address6>

[7] Testing asset: http://<target_address7>
```

### Interaction Results
The example output as seen on the interactor due to a the Log4J vulnerability being found in an asset.
```
;; ANSWER SECTION:
<targetId>.<InteractionURL>.	3600	IN	A	<IP>

;; AUTHORITY SECTION:
<targetId>.<InteractionURL>.	3600	IN	NS	ns1.<InteractionURL>.
<targetId>.<InteractionURL>.	3600	IN	NS	ns2.<InteractionURL>.
```

- `<targetId>` - represents the line number of the target in the target file

