# Changelog

All notable changes to rae-helm will be documented in this file.

## 2020-09-24

- requirements upated to latest version

- Test docker image added
- Travis integration added

## 2019-07-03

- Test docker image added
- Travis integration added

## 2019-05-19

- Schema Registry dependency added (python-schema-registry-client[faust]==0.3.0)

## 2019-04-18

- Logging now is set from `settings` and not from ENV variable

## 2019-04-17

- Settings implemented with simple-settings package.
- Faust version updated to 1.5.4

## 2019-04-04

- Integration with Schema registry finished
- Custom Codec and Serializer added
- Schema Registry client added
- New faust application called Users added.

## 2019-03-17

- First release
- `docker-compose` finished with `zookeeper`, `kafka` and `schema-registry`
- `Page views` and `Leader Election` packages added.
